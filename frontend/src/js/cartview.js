// Authentication check function
function checkAuth() {
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = 'log-in.html';
        return false;
    }
    return true;
}

// Initial auth check
if (!checkAuth()) {
    window.location.href = 'log-in.html';
}

// Navigation event listeners
document.querySelectorAll('nav button').forEach(button => {
    button.addEventListener('click', (e) => {
        if (!checkAuth()) return;
        
        const buttonText = e.target.textContent.toLowerCase().trim();
        switch(buttonText) {
            case 'browse': window.location.href = 'inventory.html'; break;
            case 'cart': window.location.href = 'cartview.html'; break;
            case 'my account': window.location.href = 'myaccount.html'; break;
            case 'log out': handleLogout(); break;
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // Check authentication when DOM loads
    if (!checkAuth()) return;

    const cartTable = document.querySelector('#cart-table tbody');
    const clearCartBtn = document.getElementById('clear-cart');
    const invoiceBtn = document.getElementById('create-invoice');

    function loadCart() {
        if (!checkAuth()) return;
        
        const cart = JSON.parse(localStorage.getItem('cart')) || [];
        cartTable.innerHTML = '';
        
        if (cart.length === 0) {
            cartTable.innerHTML = '<tr><td colspan="6">Cart is empty</td></tr>';
            return;
        }

        cart.forEach((item, index) => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${item.title}</td>
                <td>${item.isbn}</td>
                <td>£${item.price}</td>
                <td>£${item.price * item.quantity}</td>
                <td>
                    <button class="qty-btn" data-action="decrease" data-index="${index}">-</button>
                    <span>${item.quantity || 1}</span>
                    <button class="qty-btn" data-action="increase" data-index="${index}">+</button>
                </td>
                <td>
                    <button class="remove-btn" data-index="${index}">Remove</button>
                </td>
            `;
            cartTable.appendChild(row);
        });

        updateTotal(cart);
    }

    function updateTotal(cart) {
        const total = cart.reduce((sum, item) => 
            sum + (parseFloat(item.price) * (item.quantity || 1)), 0
        );
        invoiceBtn.textContent = `Create Invoice (£${total.toFixed(2)})`;
    }

    function updateCart(cart) {
        if (!checkAuth()) return;
        localStorage.setItem('cart', JSON.stringify(cart));
        loadCart();
    }

    // Event delegation for cart actions
    document.addEventListener('click', (e) => {
        if (!checkAuth()) return;

        if (e.target.matches('.qty-btn')) {
            const cart = JSON.parse(localStorage.getItem('cart')) || [];
            const index = parseInt(e.target.dataset.index);
            const action = e.target.dataset.action;

            if (action === 'increase') {
                cart[index].quantity = (cart[index].quantity || 1) + 1;
            } else if (action === 'decrease' && cart[index].quantity > 1) {
                cart[index].quantity--;
            }

            updateCart(cart);
        }

        if (e.target.matches('.remove-btn')) {
            const cart = JSON.parse(localStorage.getItem('cart')) || [];
            const index = parseInt(e.target.dataset.index);
            cart.splice(index, 1);
            updateCart(cart);
        }
    });

    clearCartBtn.addEventListener('click', () => {
        if (!checkAuth()) return;
        localStorage.removeItem('cart');
        loadCart();
    });

    // Add event listener for invoice button
    invoiceBtn.addEventListener('click', () => {
        if (!checkAuth()) return;
        const cart = JSON.parse(localStorage.getItem('cart')) || [];
        if (cart.length === 0) {
            alert('Cannot create invoice for empty cart');
            return;
        }
        // Add your invoice creation logic here
    });

    // Load cart when page initializes
    loadCart();
});

// Logout functionality
async function handleLogout() {
    try {
        localStorage.clear();
        sessionStorage.clear();
        await fetch('/auth/logout', { method: 'POST', credentials: 'include' });
    } catch (error) {
        console.error('Logout error:', error);
    } finally {
        window.location.href = 'log-in.html';
    }
}