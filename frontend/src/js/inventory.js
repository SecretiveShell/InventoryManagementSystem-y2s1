document.getElementById("prev-page").addEventListener("click", () => {
  alert("Previous Page (Not Implemented)");
});

document.getElementById("next-page").addEventListener("click", () => {
  alert("Next Page (Not Implemented)");
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

// TODO: make this actually work
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".add-to-basket-btn").forEach((button) => {
    button.addEventListener("click", () => {
      alert("Item added");
    });
  });
});

// Edit button functionality
// TODO: make this actually work
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

// add items to list

(async () => {
  const response = await fetch("/api/inventory/list");
  const books = await response.json();

  books.forEach((book) => {
    const row = document.createElement("tr");

    const isbnCell = document.createElement("td");
    isbnCell.textContent = book.ISBN;
    row.appendChild(isbnCell);

    const titleCell = document.createElement("td");
    titleCell.textContent = book.title;
    row.appendChild(titleCell);

    const quantityCell = document.createElement("td");
    quantityCell.textContent = book.quantity;
    row.appendChild(quantityCell);

    const priceCell = document.createElement("td");
    priceCell.textContent = book.price;
    row.appendChild(priceCell);

    const locationCell = document.createElement("td");
    locationCell.textContent = book.location;
    row.appendChild(locationCell);

    const authorCell = document.createElement("td");
    authorCell.textContent = book.author;
    row.appendChild(authorCell);

    const editButtonCell = document.createElement("td");
    const editButton = document.createElement("button");
    editButton.classList.add("edit-btn");
    editButton.textContent = "Edit";
    editButtonCell.appendChild(editButton);
    row.appendChild(editButtonCell);

    const addButtonCell = document.createElement("td");
    const addButton = document.createElement("button");
    addButton.classList.add("add-to-basket-btn");
    addButton.textContent = "Add to Basket";
    addButtonCell.appendChild(addButton);
    row.appendChild(addButtonCell);

    document.getElementById("book-table").appendChild(row);
  });
})();
