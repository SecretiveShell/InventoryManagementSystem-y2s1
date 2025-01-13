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
    if (!checkAuth()) return;

    const cartTable = document.querySelector('#cart-table tbody');
    const clearCartBtn = document.getElementById('clear-cart');
    const invoiceBtn = document.getElementById('create-invoice');
    const customerForm = document.getElementById('customer-details');

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
                <td>£${(item.price * item.quantity).toFixed(2)}</td>
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
        return total;
    }

    function updateCart(cart) {
        if (!checkAuth()) return;
        localStorage.setItem('cart', JSON.stringify(cart));
        loadCart();
    }

    function getCustomerDetails() {
        return {
            name: document.getElementById('customer-name').value,
            addressLine1: document.getElementById('address-line1').value,
            addressLine2: document.getElementById('address-line2').value,
            city: document.getElementById('city').value,
            postcode: document.getElementById('postcode').value
        };
    }

    function createInvoicePreview(cart, customerDetails, total) {
        const printWindow = window.open('', '_blank');
        printWindow.document.write(`
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Invoice - Books4Bucks</title>
                    <style>
                        body { 
                            font-family: Arial, sans-serif; 
                            padding: 20px;
                            max-width: 800px;
                            margin: 0 auto;
                            background-color: #f4f4f4;
                        }
                        .invoice-container {
                            background-color: white;
                            padding: 40px;
                            border-radius: 8px;
                            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                        }
                        .invoice-header { text-align: center; margin-bottom: 30px; }
                        .customer-details { margin-bottom: 20px; }
                        table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
                        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                        .total { text-align: right; font-weight: bold; margin-top: 20px; }
                        .no-print button {
                            background-color: #4caf50;
                            color: white;
                            border: none;
                            padding: 10px 20px;
                            border-radius: 4px;
                            cursor: pointer;
                            margin-top: 20px;
                        }
                        .no-print button:hover {
                            background-color: #45a049;
                        }
                        @media print {
                            body {
                                background-color: white;
                                padding: 0;
                            }
                            .invoice-container {
                                box-shadow: none;
                                padding: 0;
                            }
                            .no-print { display: none; }
                        }
                    </style>
                </head>
                <body>
                    <div class="invoice-container">
                        <div class="invoice-header">
                            <h1>Books4Bucks</h1>
                            <h2>Invoice</h2>
                        </div>
                        
                        <div class="customer-details">
                            <h3>Bill To:</h3>
                            <p>${customerDetails.name}</p>
                            <p>${customerDetails.addressLine1}</p>
                            ${customerDetails.addressLine2 ? `<p>${customerDetails.addressLine2}</p>` : ''}
                            <p>${customerDetails.city}</p>
                            <p>${customerDetails.postcode}</p>
                        </div>

                        <table>
                            <thead>
                                <tr>
                                    <th>Book</th>
                                    <th>ISBN</th>
                                    <th>Price</th>
                                    <th>Quantity</th>
                                    <th>Total</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${cart.map(item => `
                                    <tr>
                                        <td>${item.title}</td>
                                        <td>${item.isbn}</td>
                                        <td>£${item.price}</td>
                                        <td>${item.quantity || 1}</td>
                                        <td>£${(item.price * (item.quantity || 1)).toFixed(2)}</td>
                                    </tr>
                                `).join('')}
                            </tbody>
                        </table>
                        
                        <div class="total">
                            <p>Total: £${total.toFixed(2)}</p>
                        </div>
                        
                        <div class="no-print">
                            <button onclick="window.print()">Print Invoice</button>
                        </div>
                    </div>
                </body>
            </html>
        `);
        printWindow.document.close();
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

    invoiceBtn.addEventListener('click', () => {
        if (!checkAuth()) return;
        
        const cart = JSON.parse(localStorage.getItem('cart')) || [];
        if (cart.length === 0) {
            alert('Cannot create invoice for empty cart');
            return;
        }

        const customerDetails = getCustomerDetails();
        if (!customerDetails.name || !customerDetails.addressLine1 || !customerDetails.city || !customerDetails.postcode) {
            alert('Please fill in all required customer details (name, address line 1, city, and postcode)');
            return;
        }

        const total = updateTotal(cart);
        createInvoicePreview(cart, customerDetails, total);
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