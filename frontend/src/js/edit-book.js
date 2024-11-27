document.addEventListener("DOMContentLoaded", () => {
  // Retrieve book details from localStorage
  const currentBook = JSON.parse(localStorage.getItem("currentBook"));

  if (currentBook) {
    // Populate form fields
    document.getElementById("isbn").value = currentBook.isbn;
    document.getElementById("title").value = currentBook.title;
    document.getElementById("quantity").value = currentBook.quantity.replace(
      /[^\d]/g,
      "",
    );
    document.getElementById("price").value = currentBook.price;
    document.getElementById("location").value = currentBook.location;
    document.getElementById("author").value = currentBook.author;
  }

  // Form submission handling
  document.getElementById("edit-book-form").addEventListener("submit", (e) => {
    e.preventDefault();

    // Collect form data
    const updatedBook = {
      isbn: document.getElementById("isbn").value,
      title: document.getElementById("title").value,
      quantity: document.getElementById("quantity").value,
      price: document.getElementById("price").value,
      location: document.getElementById("location").value,
      author: document.getElementById("author").value,
    };

    // In a real application, this would send data to backend
    alert("Changes saved:\n" + JSON.stringify(updatedBook, null, 2));

    // Clear localStorage and return to main page
    localStorage.removeItem("currentBook");
    window.location.href = "inventory.html";
  });
});
