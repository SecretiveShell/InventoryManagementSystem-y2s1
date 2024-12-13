document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();  // Prevent default form submission (prevents leaking passwords in the URL) 
  
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const data = {
      email: email,
      password: password
    };
  
    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
  
      const result = await response.json();
  
      if (result.success) {
        // Handle login success
        localStorage.setItem('token', result.token);
        window.location.href = 'inventory.html';
      } else {
        // Handle login failure
        alert('Login failed. Please check your credentials.');
      }
    } catch (error) {
      alert('Error during login. Please try again later.');
    }
  });
  