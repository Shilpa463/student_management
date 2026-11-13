
# Student Management System

A mini Student Management System developed using Python, SQLite, Pydantic, FastAPI, Streamlit and Git.

## Features

- Add student records.
- View all students.
- Delete students using Student ID.
- Validate student information using Pydantic.
- Validate marks between 0 and 100.
- Calculate average student marks.
- Store student data in SQLite.

## Technologies Used

- Python
- SQLite
- Pydantic
- FastAPI
- Streamlit
- Git and GitHub

## Project Structure

```text
student_management/
│
├── database.py
├── models.py
├── main.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Open the project folder:

```bash
cd student_management
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open API documentation:

http://127.0.0.1:8000/docs

Open another terminal and run Streamlit:

```bash
streamlit run streamlit_app.py
```

Open the application:

http://localhost:8501

## Database

The project uses SQLite to store student records in students.db.

The database and students table are created automatically when the FastAPI application starts.

## Author

Student Management System Mini Project
