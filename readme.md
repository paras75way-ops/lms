Learning Management System (LMS) – Backend

Author: Paras Ohri

This project is a backend API for a Learning Management System (LMS). It is built using FastAPI and follows a layered architecture with routers, services, and repositories. The system supports user authentication, role-based access control, course management, and student enrollment.

Tech Stack

Python 3.13

FastAPI

SQLModel

PostgreSQL

Alembic

JWT Authentication

Project Features

User authentication using JWT

Role-based access (Admin, Instructor, Student)

Course creation and management

Student enrollment

Learning progress tracking

Database migrations using Alembic

Interactive API documentation using Swagger

Project Setup Instructions
1. Clone the Repository
git clone https://github.com/paras75way-ops/lms.git
cd assesment
2. Create and Activate Virtual Environment

macOS / Linux:

python3 -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt
4. Environment Variables Configuration

Create a .env file in the project root directory:

DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/lms_db
SECRET_KEY=your_secret_key_here
 

The .env file is required to run the project and is intentionally not committed to version control.

5. Database Migration

Run the following command to apply database migrations:

alembic upgrade head

 
6. Run the Application
uvicorn app.main:app --reload

The application will start at:

http://127.0.0.1:8000
API Documentation

Swagger UI:

http://127.0.0.1:8000/docs



Login endpoint:

POST /api/auth/login

The login endpoint accepts email and password

On successful login, an access token and refresh token are returned

Protected routes require a valid JWT access token

To authorize in Swagger:

Click the "Authorize" button

Enter the username and password


 

Ensure PostgreSQL is running before starting the application

The .env file must be present for the application to start

All endpoints can be tested using Swagger UI

Future Improvements

Video upload support

Rate limiting on authentication endpoints

Docker support

