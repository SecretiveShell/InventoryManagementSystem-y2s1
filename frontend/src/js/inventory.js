document.addEventListener('DOMContentLoaded', () => {
    const bookTableBody = document.querySelector('#book-table tbody');
    const prevPageBtn = document.getElementById('prev-page');
    const nextPageBtn = document.getElementById('next-page');
    const searchBar = document.getElementById("search-bar");
  
    let currentPage = 1;
    let totalPages = 1;
    let allBooks = []; // Store all books
    let filteredBooks = []; // Store filtered books
    const PAGE_SIZE = 7;
  
    // Function to fetch books from the API
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
  
    // Function to fetch all books across all pages
    async function fetchAllBooks() {
      try {
          // First, get the total number of pages
          const firstPageData = await fetchBooks(1);
          if (!firstPageData) return [];
  
          totalPages = firstPageData.total_pages;
          allBooks = firstPageData.books;
  
          // Fetch books from remaining pages
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
  
    // Function to populate the table with books
    function populateBookTable(books) {
        // Clear existing rows
        bookTableBody.innerHTML = '';
  
        // Populate table with new books
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
  
        // Add event listeners to new edit and add to basket buttons
        addBookActionListeners();
    }
  
    // Function to update pagination buttons
    function updatePaginationButtons(currentPage, totalPages) {
        prevPageBtn.disabled = currentPage === 1;
        nextPageBtn.disabled = currentPage === totalPages;
    }
  
    // Load books for the current page
    async function loadBooks(page) {
        const bookData = await fetchBooks(page);
        if (bookData) {
            populateBookTable(bookData.books);
            currentPage = bookData.current_page;
            totalPages = bookData.total_pages;
            updatePaginationButtons(currentPage, totalPages);
        }
    }
  
    // Event listeners for pagination buttons
    prevPageBtn.addEventListener('click', () => {
        if (currentPage > 1) {
            if (filteredBooks.length > 0) {
                // If in search mode, paginate filtered books
                const startIndex = (currentPage - 2) * PAGE_SIZE;
                const endIndex = (currentPage - 1) * PAGE_SIZE;
                populateBookTable(filteredBooks.slice(startIndex, endIndex));
                currentPage--;
                updatePaginationButtons(currentPage, Math.ceil(filteredBooks.length / PAGE_SIZE));
            } else {
                // Normal pagination for full inventory
                loadBooks(currentPage - 1);
            }
        }
    });
  
    nextPageBtn.addEventListener('click', () => {
        if (filteredBooks.length > 0) {
            // If in search mode, paginate filtered books
            const startIndex = currentPage * PAGE_SIZE;
            const endIndex = (currentPage + 1) * PAGE_SIZE;
            if (startIndex < filteredBooks.length) {
                populateBookTable(filteredBooks.slice(startIndex, endIndex));
                currentPage++;
                updatePaginationButtons(currentPage, Math.ceil(filteredBooks.length / PAGE_SIZE));
            }
        } else {
            // Normal pagination for full inventory
            if (currentPage < totalPages) {
                loadBooks(currentPage + 1);
            }
        }
    });
  
    // Search functionality 
    async function performSearch() {
        const searchTerm = searchBar.value.toLowerCase();
  
        // Ensure all books are loaded
        if (allBooks.length === 0) {
            await fetchAllBooks();
        }
  
        // Filter books based on search term, removing duplicates
        const uniqueBookSet = new Set();
        filteredBooks = allBooks.filter(book => {
            // Convert all book values to lowercase strings for comparison
            const bookValues = Object.values(book).map(value => 
                value.toString().toLowerCase()
            );
            
            // Check if any value matches the search term
            const isMatch = bookValues.some(value => 
                value.includes(searchTerm)
            );
            
            // Use ISBN as a unique identifier to remove duplicates
            if (isMatch) {
                if (!uniqueBookSet.has(book.ISBN)) {
                    uniqueBookSet.add(book.ISBN);
                    return true;
                }
            }
            
            return false;
        });
  
        // Reset to first page of search results
        currentPage = 1;
  
        // Populate first page of filtered books
        const firstPageBooks = filteredBooks.slice(0, PAGE_SIZE);
        populateBookTable(firstPageBooks);
  
        // Update pagination for search results
        updatePaginationButtons(currentPage, Math.ceil(filteredBooks.length / PAGE_SIZE));
    }
  
    // Add search event listener
    searchBar.addEventListener("input", performSearch);
  
    // Initial load of books
    loadBooks(1);
});



// Edit button functionality
function addBookActionListeners() {
    // Edit button handler
    document.querySelectorAll(".edit-btn").forEach((button) => {
        button.addEventListener("click", () => {
            const row = button.closest("tr");
            const bookDetails = {
                isbn: row.cells[0].textContent,
                title: row.cells[1].textContent,
                quantity: row.cells[2].textContent,
                price: row.cells[3].textContent,
                location: row.cells[4].textContent,
                author: row.cells[5].textContent,
            };
            
            // Store book details in localStorage to pass to edit page
            localStorage.setItem("currentBook", JSON.stringify(bookDetails));
            
            // Redirect to edit page
            window.location.href = "edit-book.html";
        });
    });

    // Add to basket button handler
    document.querySelectorAll(".add-to-basket-btn").forEach((button) => {
        button.addEventListener("click", () => {
            alert("Item added");
        });
    });
}

// Navigation Button Event Listeners
document.querySelectorAll('nav button').forEach(button => {
    button.addEventListener('click', (e) => {
        const buttonText = e.target.textContent.toLowerCase();
        
        switch(buttonText) {
            case 'browse':
                window.location.href = 'inventory.html';
                break;
            case 'cart':
                window.location.href = 'cartview.html';
                break;
            case 'my account':
                // TODO: Implement my account page navigation
                console.log('Navigate to My Account');
                break;
            case 'log out':
                handleLogout();
                break;
        }
    });
});

// Logout Functionality
function handleLogout() {
    try {
        // Clear any stored authentication tokens
        localStorage.removeItem('authToken');
        sessionStorage.removeItem('authToken');
        
        // Call backend logout endpoint if exists
        fetch('/auth/logout', {
            method: 'POST',
            credentials: 'include' // Important for sending cookies
        })
        .catch(error => {
            console.error('Logout API call failed:', error);
        })
        .finally(() => {
            // Always redirect to login page
            window.location.href = 'login.html';
        });
    } catch (error) {
        console.error('Logout error:', error);
        window.location.href = 'login.html';
    }
}