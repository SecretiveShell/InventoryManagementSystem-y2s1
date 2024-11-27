document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");

  loginForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!email || !password) {
      alert("Please enter both email and password");
      return;
    }

    // remove later - only for demonstaration
    if (email === "user@a.com" && password === "12345678") {
      window.location.href = "inventory.html";
    } else {
      alert("Invalid email or password");
    }
  });
});
