# 📚 LMS Student Management System  
FastAPI + PostgreSQL + Flask

---

## 🚀 Project Overview

This project is a **Student Learning Management System (LMS)** that performs full **CRUD operations** (Create, Read, Update, Delete) on student records using:

- FastAPI (Backend API)
- PostgreSQL (Database)
- SQLAlchemy (ORM)
- Flask (Frontend UI)
- HTML & CSS (UI Design)

The system allows users to manage student data through a simple and interactive dashboard.

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| FastAPI | Backend REST API |
| PostgreSQL | Relational Database |
| SQLAlchemy | ORM for DB interaction |
| Pydantic | Data validation |
| Uvicorn | ASGI server |
| Flask | Frontend UI |
| HTML & CSS | UI Design |
| Requests Library | Communication between Flask & FastAPI |

## 📁 Project Structure

```
LMS_Project/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   ├── routes.py
│   │
│   └── venv/
│
├── frontend/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── add.html
│   │   ├── edit.html
│   │
│   └── static/
│       ├── dashboard.css
│       ├── add.css
│
└── README.md
```

## ⚙️ Features

- ✅ Add Student
- ✅ View All Students
- ✅ Edit Student
- ✅ Delete Student
- ✅ Clean Dashboard UI
- ✅ REST API with Swagger Documentation

---

## 🗄 Database Schema

### Table: students

| Column | Type | Description |
|--------|------|------------|
| id | Integer (Primary Key) | Unique ID |
| name | String | Student Name |
| email | String (Unique) | Student Email |
| course | String | Course Name |

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /students | Add new student |
| GET | /students | Get all students |
| GET | /students/{id} | Get student by ID |
| PUT | /students/{id} | Update student |
| DELETE | /students/{id} | Delete student |

Swagger Documentation:  

http://127.0.0.1:8000/docs


---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/shivam-9s/LMS_Project.git

cd LMS_Project
```
### 2️⃣ Setup Backend
```cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy psycopg2 pydantic
uvicorn app.main:app --reload
```

Backend runs at:

http://127.0.0.1:8000

### 3️⃣ Setup Frontend

Open new terminal:

cd frontend
pip install flask requests
python app.py

Frontend runs at:

http://127.0.0.1:5000

### 4️⃣ Setup PostgreSQL

Install PostgreSQL

Create database:

CREATE DATABASE lms_db;


Update database credentials in:

backend/app/database.py


Example:

DATABASE_URL = "postgresql://postgres:YourPassword@localhost:5432/lms_db"

### 🔄 Project Workflow
User interacts with Flask UI

Flask sends request to FastAPI backend

FastAPI processes request

SQLAlchemy interacts with PostgreSQL

Response is displayed on dashboard

<img width="1925" height="894" alt="image" src="https://github.com/user-attachments/assets/322d99fb-0f8c-416f-b9ba-f4b5dab1cc4e" />


<img width="1921" height="891" alt="image" src="https://github.com/user-attachments/assets/b947fba9-fb0c-4d6f-b419-c336e0f97f44" />


<img width="1911" height="886" alt="image" src="https://github.com/user-attachments/assets/155f5fa9-f2cb-447a-a6d4-3a84938d9549" />


<img width="1926" height="889" alt="image" src="https://github.com/user-attachments/assets/812ab13c-2d4e-4e25-85d1-c402eacc558d" />



