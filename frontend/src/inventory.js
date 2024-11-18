document.addEventListener('DOMContentLoaded', () => {
    // Pagination placeholders
    document.getElementById('prev-page').addEventListener('click', () => {
        alert('Previous Page (Not Implemented)');
    });

    document.getElementById('next-page').addEventListener('click', () => {
        alert('Next Page (Not Implemented)');
    });

    // Search functionality
    document.getElementById('search-bar').addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        const rows = document.querySelectorAll('#book-table tbody tr');
        
        rows.forEach(row => {
            const text = row.textContent.toLowerCase();
            row.style.display = text.includes(searchTerm) ? '' : 'none';
        });
    });

    // Edit button functionality
    document.querySelectorAll('.edit-btn').forEach((button) => {
        button.addEventListener('click', () => {
            const row = button.closest('tr');
            const bookDetails = {
                isbn: row.cells[0].textContent,
                title: row.cells[1].textContent,
                quantity: row.cells[2].textContent,
                price: row.cells[3].textContent,
                location: row.cells[4].textContent,
                author: row.cells[5].textContent
            };

            // Store book details in localStorage to pass to edit page
            localStorage.setItem('currentBook', JSON.stringify(bookDetails));
            
            // Redirect to edit page
            window.location.href = 'edit-book.html';
        });
    });
});