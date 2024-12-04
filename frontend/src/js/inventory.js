document.addEventListener('DOMContentLoaded', () => {
    const bookTableBody = document.querySelector('#book-table tbody');
    const prevPageBtn = document.getElementById('prev-page');
    const nextPageBtn = document.getElementById('next-page');
    const searchBar = document.getElementById("search-bar");
  
    let currentPage = 1;
    let totalPages = 1;
    let allBooks = [];
    let filteredBooks = [];
    const PAGE_SIZE = 7;
  
    async function fetchBooks(page = 1) {
        try {
            const response = await fetch(`/api/inventory/list?page=${page}&page_size=7`);
            if (!response.ok) throw new Error('Failed to fetch books');
            return await response.json();
        } catch (error) {
            console.error('Error fetching books:', error);
            alert('Failed to load books. Please try again later.');
            return null;
        }
    }
  
    async function fetchAllBooks() {
        try {
            const firstPageData = await fetchBooks(1);
            if (!firstPageData) return [];
  
            totalPages = firstPageData.total_pages;
            allBooks = firstPageData.books;
  
            for (let page = 2; page <= totalPages; page++) {
                const pageData = await fetchBooks(page);
                if (pageData) allBooks = allBooks.concat(pageData.books);
            }
            return allBooks;
        } catch (error) {
            console.error('Error fetching all books:', error);
            return [];
        }
    }
  
    function populateBookTable(books) {
        bookTableBody.innerHTML = '';
        books.forEach(book => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${book.ISBN}</td>
                <td>${book.title}</td>
                <td>${book.quantity_in_stock}</td>
                <td>£${book.price}</td>
                <td>${book.location}</td>
                <td>${book.author}</td>
                <td><button class="edit-btn" data-book='${JSON.stringify(book)}'>Edit</button></td>
                <td><button class="add-to-basket-btn" data-book='${JSON.stringify(book)}'>Add to Basket</button></td>
            `;
            bookTableBody.appendChild(row);
        });
        initializeBookActionButtons();
    }
  
    function updatePaginationButtons(currentPage, totalPages) {
        prevPageBtn.disabled = currentPage === 1;
        nextPageBtn.disabled = currentPage === totalPages;
    }
  
    async function loadBooks(page) {
        const bookData = await fetchBooks(page);
        if (bookData) {
            populateBookTable(bookData.books);
            currentPage = bookData.current_page;
            totalPages = bookData.total_pages;
            updatePaginationButtons(currentPage, totalPages);
        }
    }

    function handlePagination(event) {
        const direction = event.target.id === 'prev-page' ? 'prev' : 'next';
        
        if (direction === 'prev' && currentPage > 1) {
            if (filteredBooks.length > 0) {
                const startIndex = (currentPage - 2) * PAGE_SIZE;
                const endIndex = (currentPage - 1) * PAGE_SIZE;
                populateBookTable(filteredBooks.slice(startIndex, endIndex));
                currentPage--;
            } else {
                loadBooks(currentPage - 1);
            }
        } else if (direction === 'next') {
            if (filteredBooks.length > 0) {
                const startIndex = currentPage * PAGE_SIZE;
                const endIndex = (currentPage + 1) * PAGE_SIZE;
                if (startIndex < filteredBooks.length) {
                    populateBookTable(filteredBooks.slice(startIndex, endIndex));
                    currentPage++;
                }
            } else if (currentPage < totalPages) {
                loadBooks(currentPage + 1);
            }
        }
        
        updatePaginationButtons(currentPage, Math.ceil(
            (filteredBooks.length > 0 ? filteredBooks.length : totalBooks) / PAGE_SIZE
        ));
    }

    async function performSearch() {
        const searchTerm = searchBar.value.toLowerCase();
        if (allBooks.length === 0) await fetchAllBooks();
  
        const uniqueBookSet = new Set();
        filteredBooks = allBooks.filter(book => {
            const bookValues = Object.values(book).map(value => 
                value.toString().toLowerCase()
            );
            const isMatch = bookValues.some(value => value.includes(searchTerm));
            if (isMatch && !uniqueBookSet.has(book.ISBN)) {
                uniqueBookSet.add(book.ISBN);
                return true;
            }
            return false;
        });
  
        currentPage = 1;
        populateBookTable(filteredBooks.slice(0, PAGE_SIZE));
        updatePaginationButtons(currentPage, Math.ceil(filteredBooks.length / PAGE_SIZE));
    }

    function initializeBookActionButtons() {
        document.querySelectorAll('.edit-btn').forEach(button => {
            button.addEventListener('click', async (e) => {
                const bookData = JSON.parse(e.target.dataset.book);
                try {
                    localStorage.setItem('currentBook', JSON.stringify(bookData));
                    e.target.textContent = 'Editing...';
                    e.target.disabled = true;
                    window.location.href = 'edit-book.html';
                } catch (error) {
                    console.error('Error:', error);
                    e.target.textContent = 'Edit';
                    e.target.disabled = false;
                    alert('Failed to open edit page');
                }
            });
        });

        document.querySelectorAll('.add-to-basket-btn').forEach(button => {
            button.addEventListener('click', (e) => {
                const bookData = JSON.parse(e.target.dataset.book);
                const cart = JSON.parse(localStorage.getItem('cart')) || [];
                const existingItem = cart.find(item => item.isbn === bookData.ISBN);
                
                if (existingItem) {
                    existingItem.quantity = (existingItem.quantity || 1) + 1;
                } else {
                    cart.push({
                        isbn: bookData.ISBN,
                        title: bookData.title,
                        price: bookData.price,
                        quantity: 1
                    });
                }
                
                localStorage.setItem('cart', JSON.stringify(cart));
                e.target.textContent = 'Added!';
                e.target.disabled = true;
                
                setTimeout(() => {
                    e.target.textContent = 'Add to Basket';
                    e.target.disabled = false;
                }, 1000);
            });
        });
    }

    async function handleLogout() {
        try {
            localStorage.clear();
            sessionStorage.clear();
            await fetch('/auth/logout', { method: 'POST', credentials: 'include' });
        } catch (error) {
            console.error('Logout error:', error);
        } finally {
            window.location.href = 'login.html';
        }
    }

    prevPageBtn.addEventListener('click', handlePagination);
    nextPageBtn.addEventListener('click', handlePagination);
    searchBar.addEventListener("input", performSearch);

    document.querySelectorAll('nav button').forEach(button => {
        button.addEventListener('click', (e) => {
            const buttonText = e.target.textContent.toLowerCase().trim();
            switch(buttonText) {
                case 'browse': window.location.href = 'inventory.html'; break;
                case 'cart': window.location.href = 'cartview.html'; break;
                case 'my account': window.location.href = 'myaccount.html'; break;
                case 'log out': handleLogout(); break;
            }
        });
    });

    loadBooks(1);
});