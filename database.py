import sqlite3

DB_NAME = "students.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL,
            marks REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_student(student):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (id, name, age, email, marks)
        VALUES (?, ?, ?, ?, ?)
    """, (
        student.id,
        student.name,
        student.age,
        student.email,
        student.marks
    ))

    conn.commit()
    conn.close()


def get_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "email": row[3],
            "marks": row[4]
        }
        for row in rows
    ]


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    deleted = cursor.rowcount

    conn.commit()
    conn.close()

    return deleted