Namw : Om Kumar Jha
Uid :23BCC70012
Experiment: Student CRUD API Development
1. Aim
To design and implement a backend server using the Flask framework in Python to perform CRUD (Create, Read, Update, Delete) operations on a MySQL database, and to validate the API endpoints using Postman.

2. Procedure
Phase 1: Environment Setup
Install the Python interpreter and set up a virtual environment.

Install necessary libraries: flask, flask-sqlalchemy, and pymysql.

Set up a MySQL server and create a database (e.g., university_db).

Phase 2: Database Schema Design
Define a table named student with the following attributes:

id (Primary Key, Auto-increment)

name (Varchar)

email (Varchar, Unique)

course (Varchar)

Phase 3: Backend Implementation
Initialization: Configure the Flask app and link it to the MySQL database using SQLAlchemy.

Model Definition: Create a Python class representing the student table.

API Development:

Implement a POST method to insert new student data.

Implement a GET method to fetch and display records.

Implement a PUT method to modify existing student information.

Implement a DELETE method to remove records by ID.

Phase 4: Testing & Documentation
Run the Flask server (typically on localhost:5000).

Open Postman and create requests for each endpoint (GET, POST, PUT, DELETE).

Verify that changes in Postman are reflected in the MySQL Database table.

Create a README.md file detailing the setup and usage instructions.

3. Learning Outcomes
By the end of this experiment, you will be able to:

Architect RESTful Services: Understand the structure of REST APIs and how to map HTTP methods to database operations.

Database Integration: Gain hands-on experience in connecting a Python backend to a relational database (MySQL) using an ORM (Object-Relational Mapping).

API Testing Mastery: Proficiency in using Postman for debugging, sending JSON payloads, and inspecting server responses.

Full-Stack Workflow: Comprehend the data flow between a client (Postman), a server (Flask), and a storage layer (MySQL).

Documentation Skills: Learn to document technical projects effectively using Markdown for better collaboration and version control.