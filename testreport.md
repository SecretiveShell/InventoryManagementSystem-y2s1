# Testing Report

Project: (Business) Inventory Management System 
Group #: 15

Date:  27/11/2024
 
<br>Table of Contents:
<br>Introduction	
<br>Test strategy	
<br>Objectives	
<br>Scope	
<br>Unit Testing	
<br>Test Cases	
<br>Non-Functional Requirements testing	
<br>Appendix 1: Defect report	



 
## Introduction
Briefly Describe the report's purpose.

To evaluate the reliability of the functionalities of different user interaction pages: Sign Up, Log-In, Reset Password, and Invoices Pages. This testing process aims to ensure that these buttons perform as expected across multiple devices, web browsers, and under various conditions to provide a smooth user experience 
Test strategy
Provide a clear overview of your application's testing approach, detailing the methods and tools utilized. Specify which tests were conducted manually and which were automated, highlighting the rationale behind these choices.

Zap will be utilised to carry out rigorous testing of the different components 
JMeter will used to carry out load testing  
To ensure comprehensive testing, a mix of manual and automated testing approaches were employed. Unit tests were conducted using the pytest framework to validate the individual functions tied to button operations, ensuring the correct response to user input. Manual testing was carried out to evaluate the user interface's responsiveness and overall usability on a web browser.

## Testing Tools:
<br>Unit Testing: pytest
<br>Linting/Formatting: ruff (integrated with GitHub Actions for automated CI/CD pipeline)
<br>Accessibility: Lighthouse for automated accessibility checks

       
## Objectives
Write a list of testing objectives for this project, such as:
•	Ensure compliance with accessibility standards for users with disabilities.
Ensure all button functionalities (click, hover, and response) are working as intended across the Log-in, Sign-up, Reset Password, and Invoices pages.
Scope
Define the scope of your testing, this can include:
Features to Be Tested, Testing Types, which web browsers are used for manual testing, and constraints such as time.
Features to Be Tested:
Button functionalities, including click and hover actions, form submissions, and error handling for:
Log-in Page | Sign-up Page | Reset Password Page | Invoices Page
Manual functional tests were performed on Google Chrome. This approach was taken to validate the behaviour of buttons under real-world usage scenarios.

## Unit Testing
Indicate if you have done unit testing. Which testing Framework have you used.
Include a link to Unit testing code on get hub.
 
Test button functionalities in the Log-in, Sign up, Reset Password and Invoices page 

## Test Cases
Write test cases based on your user stories acceptance criteria (update the user stories accordingly). 
Use the following template.
| Test | Information |
| --- | --- |
| Test Case ID | TC001 |
| Test Description | Verify that a user can successfully interact with the systems buttons | 
| Pre-Conditions | The buttons for the navigation pages are accessible and properly displayed |
| Steps to Execute | 1.	Navigate to the sign-up form page.  <br>2.	Enter a valid first name (e.g., "John"). <br> 3.	Enter a valid last name (e.g., "Doe"). <br>4.	Enter a valid email address (e.g., "johndoe@example.com"). <br>5.	Enter a valid password (e.g., "Password123!"). <br>6.	Confirm the password (e.g., "Password123!"). <br>7.	Click on the "Sign Up" button. |
| Expected Result |	The user should be successfully registered. <br>•	A confirmation message indicating successful sign-up is displayed.  <br>•	The entered data is saved correctly in the database. |
| Status (Pass/Fail) | Pass |
 
# Non-Functional Requirements testing
Include a sub-section with evidence for each tested non-functional requirement. E.g. Security, Performance, Usability etc. Evidence can include screenshots or links to other files like generated OWASP ZAP report for testing security.

## Appendix 1: Defect report

Include a link to your defect report (you may add this to the project GitHub repository). 
Use this template:
https://docs.google.com/spreadsheets/d/1ovkIcOcHpchVwkhitYrH7GmAdiqHCUR2LOFM-VzkFyE/edit?gid=0#gid=0

