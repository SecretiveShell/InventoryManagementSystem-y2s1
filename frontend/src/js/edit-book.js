/**
 * edit-book.js
 * Handles the editing of book inventory details
 */

document.addEventListener("DOMContentLoaded", async () => {
  // Get and populate book data
  const currentBook = JSON.parse(localStorage.getItem("currentBook"));
  console.log('Current book data:', currentBook);

  if (!currentBook) {
      console.error('No book data found in localStorage');
      alert('Error: Could not load book data');
      window.location.href = 'inventory.html';
      return;
  }

  // Populate form fields
  document.getElementById("isbn").value = currentBook.ISBN || '';
  document.getElementById("title").value = currentBook.title || '';
  document.getElementById("quantity").value = currentBook.quantity_in_stock || '';
  document.getElementById("price").value = currentBook.price || '';
  
  
  // Handle authors array
  const authorNames = currentBook.authors ? 
      currentBook.authors.map(author => author.name).join(', ') : '';
  document.getElementById("author").value = authorNames;

  // Form submission handler
  const form = document.getElementById("edit-book-form");
  if (form) {
      form.addEventListener("submit", async (e) => {
          e.preventDefault();

          // Disable save button and show loading state
          const saveButton = document.querySelector('.btn-save');
          if (saveButton) {
              saveButton.disabled = true;
              saveButton.textContent = 'Saving...';
          }

          try {
              // Get form inputs
              const quantityStr = document.getElementById("quantity").value.trim();
              const priceStr = document.getElementById("price").value.trim();
              
              // Validation
              if (!quantityStr || !priceStr) {
                  throw new Error('Quantity and price are required');
              }
              
              const quantity = parseInt(quantityStr);
              const price = parseFloat(priceStr);
              
              if (isNaN(quantity) || quantity < 0) {
                  throw new Error('Quantity must be a valid positive number');
              }

              if (isNaN(price) || price < 0) {
                  throw new Error('Price must be a valid positive number');
              }

              // Prepare update data
              const inventoryData = {
                  quantity_in_stock: quantity,
                  price: Number(price.toFixed(2))
              };

              console.log('Sending data:', JSON.stringify(inventoryData, null, 2));

              // Send request
              const response = await fetch(`/api/inventory/${currentBook.book_id}`, {
                  method: 'PUT',
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  body: JSON.stringify(inventoryData)
              });

              console.log('Response status:', response.status);

              const responseText = await response.text();
              console.log('Raw response:', responseText);

              if (!response.ok) {
                  let errorMessage;
                  try {
                      const errorData = JSON.parse(responseText);
                      errorMessage = errorData.detail || JSON.stringify(errorData);
                  } catch {
                      errorMessage = responseText || `Error: ${response.status}`;
                  }
                  throw new Error(errorMessage);
              }

              // Success - return to inventory page
              localStorage.removeItem("currentBook");
              window.location.href = "inventory.html";

          } catch (error) {
              console.error('Error saving book:', error);
              alert(`Failed to save changes: ${error.message}`);
              
              // Reset save button
              if (saveButton) {
                  saveButton.disabled = false;
                  saveButton.textContent = 'Save Changes';
              }
          }
      });
  }

  // Initialize navigation
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
});