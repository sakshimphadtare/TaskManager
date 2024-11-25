# TaskManager API

## Introduction

TaskManager is a Django-based API project that allows users to manage tasks through CRUD (Create, Read, Update, Delete) operations. The API supports token-based authentication, ensuring that only authenticated users can access and manage tasks.

## Features

- CRUD operations for task management
- Token-based authentication
- Permissions to restrict access to authenticated users
- API testing using Postman

## Technologies Used

- Python 3.x
- Django 3.x
- Django REST Framework
- SQLite (or your preferred database)
- Postman for API testing

## Setup Instructions

Follow the steps below to get the project up and running:

1. **Clone the repository**:
   
   git clone https://github.com/sakshimphadtare/TaskManager.git
   cd TaskManager
   
 **Set up a virtual environment:**


python -m venv venv
source venv/bin/activate 

**Install dependencies:**


pip install -r requirements.txt

**Apply migrations:**


python manage.py migrate

**Create a superuser (optional, for admin access):**


python manage.py createsuperuser

**Run the server:**


python manage.py runserver
Now, the project will be running at http://127.0.0.1:8000/.

## API Endpoints
**Authentication Endpoints:**
*POST /login/: Authenticate a user and get a token.*
**Request Body:**

{
  "username": "user",
  "password": "password"
}

**Response:**

{
  "token": "your_token_here"
}

**Task Endpoints:**
GET /tasks/: List all tasks. (Authenticated users only)

**Response:**

[
  {
    "id": 1,
    "title": "Test Task",
    "description": "This is a test task",
    "completed": false
  }
]

*POST /tasks/: Create a new task. (Authenticated users only)*

**Request Body:**

{
  "title": "New Task",
  "description": "This is a description",
  "completed": false
}

**Response:**

{
  "id": 2,
  "title": "New Task",
  "description": "This is a description",
  "completed": false
}

*GET /tasks/{id}/: Retrieve a task by ID. (Authenticated users only)*

Response:

{
  "id": 1,
  "title": "Test Task",
  "description": "This is a test task",
  "completed": false
}

*PUT /tasks/{id}/: Update a task by ID. (Authenticated users only)*

**Request Body:**

{
  "title": "Updated Task",
  "description": "Updated description",
  "completed": true
}

*Response:*

{
  "id": 1,
  "title": "Updated Task",
  "description": "Updated description",
  "completed": true
}

**Include the token in the Authorization header for subsequent requests to access task-related endpoints.
License
This project is licensed under the MIT License - see the LICENSE file for details.**



### Steps to Add this to Your GitHub Repository:

1. **Create the `README.md` file** in the root directory of your project.
2. **Copy** and **paste** the above content into the `README.md` file.
3. **Stage and commit the file**:
   
   git add README.md
   
   git commit -m "Add README file for TaskManager API project"
   
**Push to your GitHub repository:**

git push origin master
