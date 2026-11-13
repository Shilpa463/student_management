from fastapi import FastAPI, HTTPException
from models import Student
import database

app = FastAPI(title="Student Management System")

database.create_table()


# Add Student
@app.post("/students")
def add_student(student: Student):

    try:
        database.add_student(student)

    except Exception as e:
        if "UNIQUE constraint failed" in str(e):
            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )
        raise HTTPException(
            status_code=500,
            detail="Unable to add student"
        )

    return {"message": "Student added successfully"}


# View All Students
@app.get("/students")
def get_students():
    return database.get_students()


# Delete Student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    deleted = database.delete_student(student_id)

    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {"message": "Student deleted successfully"}