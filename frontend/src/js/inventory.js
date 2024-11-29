document.addEventListener('DOMContentLoaded', () => {
  const bookTableBody = document.querySelector('#book-table tbody');
  const prevPageBtn = document.getElementById('prev-page');
  const nextPageBtn = document.getElementById('next-page');
  
  let currentPage = 1;
  let totalPages = 1;

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
              <td>${book.quantity}</td>
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
          loadBooks(currentPage - 1);
      }
  });

  nextPageBtn.addEventListener('click', () => {
      if (currentPage < totalPages) {
          loadBooks(currentPage + 1);
      }
  });


  // Search functionality 
  document.getElementById("search-bar").addEventListener("input", (e) => {
      const searchTerm = e.target.value.toLowerCase();
      const rows = document.querySelectorAll("#book-table tbody tr");
      
      rows.forEach((row) => {
          const text = row.textContent.toLowerCase();
          row.style.display = text.includes(searchTerm) ? "" : "none";
      });
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

  // Initial load of books
  loadBooks(1);
});