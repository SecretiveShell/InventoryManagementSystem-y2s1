// Function to replace input fields and textareas with their values before printing
function printInvoice() {
  // Get elements to replace
  const dateInput = document.getElementById('invoice-date');
  const billedToTextarea = document.getElementById('billed-to');
  const fromTextarea = document.getElementById('from-address');

  // Store original values and elements
  const originalDateValue = dateInput.value;
  const originalBilledToValue = billedToTextarea.value;
  const originalFromValue = fromTextarea.value;

  // Create replacement elements
  const dateSpan = document.createElement('span');
  dateSpan.textContent = originalDateValue;

  const billedToDiv = document.createElement('div');
  billedToDiv.innerHTML = originalBilledToValue.replace(/\n/g, '<br>');

  const fromDiv = document.createElement('div');
  fromDiv.innerHTML = originalFromValue.replace(/\n/g, '<br>');

  // Replace inputs and textareas with static text
  dateInput.parentNode.replaceChild(dateSpan, dateInput);
  billedToTextarea.parentNode.replaceChild(billedToDiv, billedToTextarea);
  fromTextarea.parentNode.replaceChild(fromDiv, fromTextarea);

  // Print the invoice
  window.print();

  // Restore original elements after printing
  dateSpan.parentNode.replaceChild(dateInput, dateSpan);
  billedToDiv.parentNode.replaceChild(billedToTextarea, billedToDiv);
  fromDiv.parentNode.replaceChild(fromTextarea, fromDiv);
}

// Navigation button handlers
document.querySelectorAll('nav button').forEach(button => {
button.addEventListener('click', (e) => {
    console.log('Button clicked:', e.target.textContent);
    const buttonText = e.target.textContent.toLowerCase().trim();
    
    switch(buttonText) {
        case 'browse':
            console.log('Navigating to inventory.html');
            window.location.href = 'inventory.html';
            break;
        case 'cart':
            console.log('Navigating to cartview.html');
            window.location.href = 'cartview.html';
            break;
        case 'log out':
            console.log('Logging out');
            handleLogout();
            break;
    }
});
});

// Define handleLogout function
function handleLogout() {
  console.log('Logging out...');
  window.location.href = 'log-in.html';
}

// Add keydown listener for Ctrl + P
document.addEventListener('keydown', function (e) {
  if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
      e.preventDefault(); // Prevent the default print dialog
      printInvoice(); // Call the custom print function
  }
});
