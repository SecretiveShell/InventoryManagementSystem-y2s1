document
  .getElementById("changePasswordForm")
  .addEventListener("submit", function (e) {
    e.preventDefault();

    const oldPassword = document.getElementById("oldPassword").value;
    const newPassword = document.getElementById("newPassword").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const errorMessageEl = document.getElementById("errorMessage");

    // Reset error message
    errorMessageEl.textContent = "";

    // Validate password requirements
    const passwordValidation = validatePassword(newPassword);
    if (!passwordValidation.isValid) {
      errorMessageEl.textContent = passwordValidation.message;
      return;
    }

    // Check if new passwords match
    if (newPassword !== confirmPassword) {
      errorMessageEl.textContent = "New passwords do not match";
      return;
    }

    // Check if old and new passwords are different
    if (oldPassword === newPassword) {
      errorMessageEl.textContent =
        "New password must be different from current password";
      return;
    }

    // If all validations pass, you would typically send this to your backend
    alert("Password change successful!");
  });

function validatePassword(password) {
  // Password validation rules
  const rules = [
    {
      test: (p) => p.length >= 8,
      message: "Password must be at least 8 characters long",
    },
    {
      test: (p) => /[A-Z]/.test(p),
      message: "Password must contain at least one uppercase letter",
    },
    {
      test: (p) => /[a-z]/.test(p),
      message: "Password must contain at least one lowercase letter",
    },
    {
      test: (p) => /[0-9]/.test(p),
      message: "Password must contain at least one number",
    },
    {
      test: (p) => /[!@#$%^&*(),.?":{}|<>]/.test(p),
      message: "Password must contain at least one special character",
    },
  ];

  for (let rule of rules) {
    if (!rule.test(password)) {
      return {
        isValid: false,
        message: rule.message,
      };
    }
  }

  return { isValid: true };
}

// Navigation button handlers
document.querySelectorAll("nav button").forEach((button) => {
  button.addEventListener("click", (e) => {
    const buttonText = e.target.textContent.toLowerCase().trim();

    switch (buttonText) {
      case "browse":
        window.location.href = "inventory.html";
        break;
      case "cart":
        window.location.href = "cartview.html";
        break;
      case "my account":
        window.location.href = "myaccount.html";
        break;
      case "log out":
        handleLogout();
        break;
    }
  });
});

// Logout functionality
async function handleLogout() {
  try {
    const logoutBtn = document.querySelector('button:contains("Log Out")');
    if (logoutBtn) {
      logoutBtn.textContent = "Logging out...";
      logoutBtn.disabled = true;
    }

    localStorage.clear();
    sessionStorage.clear();

    await fetch("/auth/logout", {
      method: "POST",
      credentials: "include",
    });
  } catch (error) {
    console.error("Logout error:", error);
  } finally {
    window.location.href = "log-in.html";
  }
}

async function fetchUserData() {
  const token = localStorage.getItem("token");

  // Check if the token exists
  if (!token) {
    window.location.href = "/log-in.html";
    return;
  }

  try {
    const response = await fetch("/api/auth/me", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        token: token,
      },
    });

    if (!response.ok) {
      window.location.href = "/log-in.html";
      return;
    }

    const data = await response.json();

    console.log("User data:", data);

    const user_info = document.getElementById("user-info");

    user_info.innerHTML = `
        <p><strong>Name:</strong> ${data.name}</p>
        <p><strong>Email:</strong> ${data.email}</p>
        <p><strong>Address:</strong> ${data.address}</p>
        <p><strong>Phone Number:</strong> ${data.phone_number}</p>
        <p><strong>Admin:</strong> ${data.is_admin ? "Yes" : "No"}</p>
      `;
  } catch (error) {
    window.location.href = "/log-in.html";
  }
}

fetchUserData();
