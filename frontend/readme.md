# Inventory Management System Frontend

## Description

This is the frontend of the Inventory Management System. The frontend is built using HTML, CSS, and JavaScript, and it is designed to be responsive, adapting to different screen sizes.

### Main Files and Directories

- **index.html**: The main entry point of the frontend application. It includes a `div` with the id `app` where the application will be mounted, and a script tag that loads `main.js`.
- **main.js**: Initializes the frontend application. Currently, it sets the inner HTML of the `#app` div to "hello world" and imports `style.css`.
- **log-in.js**: Contains JavaScript code to adjust the layout of the login form and header based on the window width. This ensures the frontend is responsive.
- **sign-up.html**: Provides the structure for the sign-up page. It includes a form for user sign-up with fields for username, email, password, and password confirmation, as well as navigation links and a link to the login page.
- **reset-password.html**: Provides the structure for the password reset page. It includes a form for resetting the password with fields for email, new password, and password confirmation, as well as navigation links and a link to the login page.
- **style.css**: Contains the main CSS styles for the application.
- **desktop.css**: Contains CSS styles specific to desktop devices.
- **mobile.css**: Contains CSS styles specific to mobile devices.

### Running the Frontend

To run the frontend, navigate to the `frontend` directory and execute the following command:

```bash
cd frontend
npm run dev
```

This command will start the development server, allowing you to view and interact with the frontend application in your web browser.
