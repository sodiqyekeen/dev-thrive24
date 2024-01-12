from skillbridge.db import *
from skillbridge.models.student_model import *

""""
CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matric_no VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    department_id INT NOT NULL,
    level INT NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES department(id) ON DELETE SET NULL
"""
def get_all_students():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM student")
    students_data = cur.fetchall()
    students = []
    for student_data in students_data:
        student = Student(student_data['id'], student_data['matric_no'], student_data['first_name'], student_data['last_name'],
                          student_data['department_id'], student_data['level'], student_data['username'], student_data'password') 
        students.append(student)
    return students

def get_student_by_id(student_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM student WHERE id = ?", (student_id,))
    student_data = cur.fetchone()
    if student_data is None:
        return None
    student = Student(student_data['id'], student_data['payment_reference'], student_data['payment_status'])
    return student

def add_new_student(payment_reference):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO Student (payment_reference, payment_status) VALUES (?,?)", (payment_reference, 'paid', ))
    db.commit()
    return cur.lastrowid

def student_exists(payment_reference):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM faculty WHERE payment_reference = ?", (payment_reference,))
    student_data = cur.fetchone()
    if student_data is None:
        return False
    return True

def update_tranaction(student : Student):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE Student SET payment_reference = ?, payment_status = ?,  WHERE id = ?", (student.get_payment_reference(), student.get_payment_status(), student.get_id()))
    db.commit()

def delete_student(student_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM Student WHERE id = ?", (student_id,))
    db.commit()