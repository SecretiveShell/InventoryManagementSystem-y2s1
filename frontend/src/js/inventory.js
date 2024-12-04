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
  
    // Fetch books from API
    async function fetchBooks(page = 1) {
        try {
            const response = await fetch(`/api/inventory/list?page=${page}&page_size=7`);
            if (!response.ok) {
                throw new Error('Failed to fetch books');
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching books:', error);
            alert('Failed to load books. Please try again later.');
            return null;
        }
    }
  
    // Fetch all books across pages
    async function fetchAllBooks() {
        try {
            const firstPageData = await fetchBooks(1);
            if (!firstPageData) return [];
  
            totalPages = firstPageData.total_pages;
            allBooks = firstPageData.books;
  
            for (let page = 2; page <= totalPages; page++) {
                const pageData = await fetchBooks(page);
                if (pageData) {
                    allBooks = allBooks.concat(pageData.books);
                }
            }
            return allBooks;
        } catch (error) {
            console.error('Error fetching all books:', error);
            return [];
        }
    }
  
    // Populate table with books
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
                <td><button class="edit-btn">Edit</button></td>
                <td><button class="add-to-basket-btn">Add to Basket</button></td>
            `;
            bookTableBody.appendChild(row);
        });
  
        initializeBookActionButtons();
    }
  
    // Update pagination buttons
    function updatePaginationButtons(currentPage, totalPages) {
        prevPageBtn.disabled = currentPage === 1;
        nextPageBtn.disabled = currentPage === totalPages;
    }
  
    // Load books for current page
    async function loadBooks(page) {
        const bookData = await fetchBooks(page);
        if (bookData) {
            populateBookTable(bookData.books);
            currentPage = bookData.current_page;
            totalPages = bookData.total_pages;
            updatePaginationButtons(currentPage, totalPages);
        }
    }

    // Handle pagination
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

    // Search functionality
    async function performSearch() {
        const searchTerm = searchBar.value.toLowerCase();
  
        if (allBooks.length === 0) {
            await fetchAllBooks();
        }
  
        const uniqueBookSet = new Set();
        filteredBooks = allBooks.filter(book => {
            const bookValues = Object.values(book).map(value => 
                value.toString().toLowerCase()
            );
            
            const isMatch = bookValues.some(value => 
                value.includes(searchTerm)
            );
            
            if (isMatch) {
                if (!uniqueBookSet.has(book.ISBN)) {
                    uniqueBookSet.add(book.ISBN);
                    return true;
                }
            }
            
            return false;
        });
  
        currentPage = 1;
        const firstPageBooks = filteredBooks.slice(0, PAGE_SIZE);
        populateBookTable(firstPageBooks);
        updatePaginationButtons(currentPage, Math.ceil(filteredBooks.length / PAGE_SIZE));
    }

    // Initialize book action buttons
    function initializeBookActionButtons() {
        // Edit button handler
        document.querySelectorAll('.edit-btn').forEach(button => {
            button.addEventListener('click', async (e) => {
                const row = e.target.closest('tr');
                const bookDetails = {
                    isbn: row.cells[0].textContent,
                    title: row.cells[1].textContent,
                    quantity: row.cells[2].textContent,
                    price: row.cells[3].textContent.replace('£', ''),
                    location: row.cells[4].textContent,
                    author: row.cells[5].textContent,
                };
                
                try {
                    localStorage.setItem('currentBook', JSON.stringify(bookDetails));
                    button.textContent = 'Editing...';
                    button.disabled = true;
                    window.location.href = 'edit-book.html';
                } catch (error) {
                    console.error('Error handling edit:', error);
                    button.textContent = 'Edit';
                    button.disabled = false;
                    alert('Failed to open edit page. Please try again.');
                }
            });
        });

        // Add to basket button handler
        document.querySelectorAll('.add-to-basket-btn').forEach(button => {
            button.addEventListener('click', async (e) => {
                const row = e.target.closest('tr');
                const book = {
                    isbn: row.cells[0].textContent,
                    title: row.cells[1].textContent,
                    price: row.cells[3].textContent.replace('£', '')
                };

                try {
                    button.textContent = 'Adding...';
                    button.disabled = true;

                    let cart = JSON.parse(localStorage.getItem('cart')) || [];
                    const existingItem = cart.find(item => item.isbn === book.isbn);
                    
                    if (existingItem) {
                        existingItem.quantity = (existingItem.quantity || 1) + 1;
                    } else {
                        cart.push({ ...book, quantity: 1 });
                    }

                    localStorage.setItem('cart', JSON.stringify(cart));
                    button.textContent = 'Added';
                    
                    setTimeout(() => {
                        button.textContent = 'Add to Basket';
                        button.disabled = false;
                    }, 1000);
                } catch (error) {
                    console.error('Error adding to basket:', error);
                    button.textContent = 'Add to Basket';
                    button.disabled = false;
                    alert('Failed to add item to basket. Please try again.');
                }
            });
        });
    }

    // Navigation button handlers
    document.querySelectorAll('nav button').forEach(button => {
        button.addEventListener('click', (e) => {
            const buttonText = e.target.textContent.toLowerCase().trim();
            
            switch(buttonText) {
                case 'browse':
                    window.location.href = 'inventory.html';
                    break;
                case 'cart':
                    window.location.href = 'cartview.html';
                    break;
                case 'my account':
                    window.location.href = 'myaccount.html';
                    break;
                case 'log out':
                    handleLogout();
                    break;
            }
        });
    });

    // Logout functionality
    async function handleLogout() {
        try {
            const logoutBtn = document.querySelector('button:contains("Log Out")');
            if (logoutBtn) {
                logoutBtn.textContent = 'Logging out...';
                logoutBtn.disabled = true;
            }

            localStorage.clear();
            sessionStorage.clear();
            
            await fetch('/auth/logout', {
                method: 'POST',
                credentials: 'include'
            });
        } catch (error) {
            console.error('Logout error:', error);
        } finally {
            window.location.href = 'login.html';
        }
    }

    // Add event listeners
    prevPageBtn.addEventListener('click', handlePagination);
    nextPageBtn.addEventListener('click', handlePagination);
    searchBar.addEventListener("input", performSearch);

    // Initial load
    loadBooks(1);
});