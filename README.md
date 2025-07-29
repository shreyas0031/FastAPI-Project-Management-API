# FastAPI Project Management API

This is a backend API built using **FastAPI**, **SQLModel**, and **PostgreSQL**. It provides user authentication (JWT-based), and CRUD operations for managing projects.

## 📦 Features

- User registration and login
- Role-based authentication (`admin`, `user`)
- Project CRUD (Create, Read, Update, Delete)
- JWT authentication
- PostgreSQL database support
- Modular structure with `models`, `schemas`, `routes`

---

## 🛠️ Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/your-username/project-api.git
cd project-api
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL

Ensure PostgreSQL is installed and running. Create a database:

```sql
CREATE DATABASE projectdb;
```

### 5. Configure environment variables

Create a `.env` file:

```
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/projectdb
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Replace values with your own.

---

## ▶️ Run the Project

```bash
uvicorn main:app --reload
```

The API will be available at: [http://localhost:8000](http://localhost:8000)

Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📬 Sample POST Data

### Register User

POST `/register`

```json
{
  "username": "admin1",
  "email": "admin1@gmail.com",
  "password": "Pass@123",
  "full_name": "Admin S",
  "mobile_number": "9876543210",
  "role": "admin"
}
```

### Login

POST `/login`

```json
{
  "username": "admin1",
  "password": "Pass@123"
}
```

### Create Project

POST `/projects` (Requires Bearer Token)

```json
{
  "name": "FastAPI Implementation",
  "description": "Building APIs using FastAPI and SQLModel",
  "start_date": "2025-07-25",
  "end_date": "2025-08-01",
  "status": "ongoing"
}
```

---

## 🧪 Testing the API

Use [Postman](https://www.postman.com/) to test the API endpoints. Import the included Postman collection JSON file.

---

## 📹 Demo Video

[📺 Watch Setup & Usage Demo](https://your-demo-link.com)

> (Upload video on YouTube/Drive and paste the link here)

---

## 🧰 Dependencies

* fastapi
* sqlmodel
* psycopg2-binary
* uvicorn
* python-jose
* passlib
* python-dotenv

Install with:

```bash
pip install fastapi sqlmodel psycopg2-binary uvicorn python-jose passlib python-dotenv
```

---

## 🚀 Deployment Notes

* Make sure environment variables are set in production
* Use Gunicorn + Uvicorn for production server
* Set up Nginx + SSL for HTTPS (optional)
* Use `.env` securely

---

## 👨‍💻 Author

**Shreyas Patil**
GitHub: [@shreyaspatil31](https://github.com/shreyaspatil31)

---

## 📄 License

MIT License

```
