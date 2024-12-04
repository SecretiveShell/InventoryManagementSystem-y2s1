
document.getElementById('changePasswordForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const oldPassword = document.getElementById('oldPassword').value;
    const newPassword = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const errorMessageEl = document.getElementById('errorMessage');
    
    // Reset error message
    errorMessageEl.textContent = '';

    // Validate password requirements
    const passwordValidation = validatePassword(newPassword);
    if (!passwordValidation.isValid) {
        errorMessageEl.textContent = passwordValidation.message;
        return;
    }

    // Check if new passwords match
    if (newPassword !== confirmPassword) {
        errorMessageEl.textContent = 'New passwords do not match';
        return;
    }

    // Check if old and new passwords are different
    if (oldPassword === newPassword) {
        errorMessageEl.textContent = 'New password must be different from current password';
        return;
    }

    // If all validations pass, you would typically send this to your backend
    alert('Password change successful!');
});

function validatePassword(password) {
    // Password validation rules
    const rules = [
        { 
            test: (p) => p.length >= 8, 
            message: 'Password must be at least 8 characters long' 
        },
        { 
            test: (p) => /[A-Z]/.test(p), 
            message: 'Password must contain at least one uppercase letter' 
        },
        { 
            test: (p) => /[a-z]/.test(p), 
            message: 'Password must contain at least one lowercase letter' 
        },
        { 
            test: (p) => /[0-9]/.test(p), 
            message: 'Password must contain at least one number' 
        },
        { 
            test: (p) => /[!@#$%^&*(),.?":{}|<>]/.test(p), 
            message: 'Password must contain at least one special character' 
        }
    ];

    for (let rule of rules) {
        if (!rule.test(password)) {
            return { 
                isValid: false, 
                message: rule.message 
            };
        }
    }

    return { isValid: true };
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

