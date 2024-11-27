 // Increase Quantity
 function increaseQty(button) {
    const qtyDisplay = button.previousElementSibling;
    let currentQty = parseInt(qtyDisplay.textContent);
    qtyDisplay.textContent = currentQty + 1;
}

// Decrease Quantity
function decreaseQty(button) {
    const qtyDisplay = button.nextElementSibling;
    let currentQty = parseInt(qtyDisplay.textContent);
    if (currentQty > 1) qtyDisplay.textContent = currentQty - 1;
}

// Remove Row
function removeRow(button) {
    const row = button.closest('tr');
    row.remove();
}

// Remove from Stock
function removeFromStock() {
    const tableBody = document.getElementById('cart-table').querySelector('tbody');
    tableBody.innerHTML = ''; // Clear the entire cart
}

