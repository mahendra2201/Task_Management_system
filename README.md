Flask OTP and Task Management App

Overview

This is a Flask-based web application that provides an OTP (One-Time Password) email verification system along with task management functionality. The application allows users to:

Receive OTP via email for verification.

Verify their email using the OTP.

Create, update, and delete tasks.

Features

Landing Page: The homepage where users can start the OTP verification process.

Email OTP Verification: Users enter their name and email to receive an OTP.

OTP Validation: Users input the OTP to verify their email.

Task Management:

Add new tasks.

Update existing tasks.

Delete tasks.

Tech Stack

Backend: Flask (Python)

Frontend: HTML, CSS (via Jinja templates)

Email Service: SMTP using Gmail

Installation and Setup

Prerequisites

Python 3.7+

Flask

Installation

Clone the repository:

git clone <repository-url>
cd <repository-folder>

Install the required Python libraries:

pip install flask

Configuration

Update the from_email and server.login credentials in the code with your Gmail account details.

Enable Less Secure Apps for your Gmail account or set up an App Password if using 2FA.

Running the Application

Run the Flask application using the following command: python app.py

Application Routes

1. / (Landing Page)

Method: GET

Displays the landing page (sample.html).

2. /getdata (OTP Generation and Email Sending)

Method: POST

Accepts user name and email.

Generates a random 6-digit OTP.

Sends the OTP to the provided email address.

Redirects to the OTP validation page (sample2.html).

3. /verifyemail (OTP Verification)

Method: POST

Accepts the user-entered OTP.

Verifies the OTP.

On success: Displays the task management page (sample3.html).

On failure: Redirects back to the OTP validation page.

4. /addtask (Add a Task)

Method: POST

Accepts a task description.

Adds the task to the task list.

Displays the updated task list.

5. /updatedata (Update a Task)

Method: POST

Accepts a task ID and updated content.

Updates the task description.

Displays the updated task list.

6. /deletedata (Delete a Task)

Method: POST

Accepts a task ID to delete.

Removes the task from the list.

Displays the updated task list.

File Structure

.
├── app.py                 # Main Flask application file
├── templates/
│   ├── sample.html        # Landing page
│   ├── sample2.html       # OTP validation page
│   ├── sample3.html       # Task management page
└── README.md              # Project documentation

Usage

Navigate to the homepage (/).

Enter your name and email to receive an OTP.

Check your email for the OTP and validate it.

Once validated, you can:

Add tasks.

Update tasks.

Delete tasks.

Security Considerations

Avoid hardcoding sensitive information like email credentials. Use environment variables instead.

Use a secure password for your email account or App Passwords if applicable.

Future Improvements

Add user authentication to allow multiple users.

Store tasks in a database instead of in-memory storage.

Enhance the UI with a modern CSS framework.
