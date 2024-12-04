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
    // Add logout logic here
    window.location.href = 'log-in.html';
}
