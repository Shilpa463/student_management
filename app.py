import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Management System")
st.write("Manage student records and track academic performance.")

# Add Student Form
st.header("➕ Add New Student")

with st.form("student_form"):
    col1, col2 = st.columns(2)

    with col1:
        student_id = st.number_input(
            "Student ID", min_value=1, step=1
        )
        name = st.text_input("Student Name")
        age = st.number_input(
            "Age", min_value=5, max_value=100, step=1
        )

    with col2:
        email = st.text_input("Email")
        marks = st.number_input(
            "Marks", min_value=0.0,
            max_value=100.0, step=0.5
        )

    submitted = st.form_submit_button("Add Student")

    if submitted:
        if not name.strip() or not email.strip():
            st.error("Please enter name and email.")
        else:
            student_data = {
                "id": int(student_id),
                "name": name.strip(),
                "age": int(age),
                "email": email.strip(),
                "marks": float(marks)
            }

            try:
                response = requests.post(
                    f"{API_URL}/students",
                    json=student_data,
                    timeout=10
                )

                if response.status_code == 200:
                    st.success("Student added successfully!")
                    st.rerun()
                else:
                    st.error(response.json()["detail"])

            except requests.exceptions.RequestException:
                st.error("FastAPI server is not running.")


st.divider()

# Display Students
st.header("📋 All Students")

try:
    response = requests.get(
        f"{API_URL}/students",
        timeout=10
    )
    response.raise_for_status()

    students = response.json()

    if students:
        df = pd.DataFrame(students)

        # Dashboard metrics
        col1, col2, col3 = st.columns(3)

        col1.metric("Total Students", len(df))

        average_marks = df["marks"].mean()
        col2.metric("Average Marks", f"{average_marks:.2f}")

        col3.metric("Highest Marks", f"{df['marks'].max():.2f}")

        st.subheader("Student Records")
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        # Delete Student
        st.subheader("🗑️ Delete Student")

        student_ids = df["id"].tolist()

        selected_id = st.selectbox(
            "Select Student ID",
            student_ids
        )

        if st.button("Delete Student"):
            delete_response = requests.delete(
                f"{API_URL}/students/{selected_id}",
                timeout=10
            )

            if delete_response.status_code == 200:
                st.success("Student deleted successfully!")
                st.rerun()
            else:
                st.error("Unable to delete student.")

    else:
        st.info("No student records found. Add your first student!")

except requests.exceptions.RequestException:
    st.error("Unable to connect to FastAPI. Please start the server.")

st.divider()
st.caption("Student Management System | Built with Python, FastAPI and Streamlit")