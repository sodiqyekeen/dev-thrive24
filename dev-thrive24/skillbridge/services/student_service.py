from skillbridge.db import *
from skillbridge.models.student_model import *


def get_all_students():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM student")
    students_data = cur.fetchall()
    students = []
    for student_data in students_data:
        student = Student(student_data['id'], student_data['matric_no'], student_data['first_name'], student_data['last_name'],
                          student_data['department_id'], student_data['level'], student_data['username'], student_data['password'],
                          student_data['email']) 
        students.append(student)
    return students

def get_student_by_id(student_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM student WHERE id = ?", (student_id,))
    student_data = cur.fetchone()
    if student_data is None:
        return None
    student = Student(student_data['id'], student_data['matric_no'], student_data['first_name'], student_data['last_name'],
                          student_data['department_id'], student_data['level'], student_data['username'], student_data['password'],
                          student_data['email'])
    return student

def add_new_student(id, matric_no, first_name, last_name, department_id, level, username, password, email):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO Student (id, matric_no, first_name, last_name, department_id, level, username, password, email) VALUES (?,?,?,?,?,?,?,?,?)", 
                (id, matric_no, first_name, last_name, department_id, level, username, password, email,))
    db.commit()
    return cur.lastrowid

def student_exists(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM faculty WHERE id = ?", (id,))
    student_data = cur.fetchone()
    if student_data is None:
        return False
    return True

def update_student(student : Student):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE Student SET id = ?, matric_no = ?, first_name = ?, last_name = ?, department_id = ?, level = ?, username = ?, password = ?, email = ?", 
                (student.get_id, student.matric_no, student.first_name, student.last_name, student.department_id, student.get_level, student.get_username, student.get_password, student.get_email))
    db.commit()

def delete_student(student_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM Student WHERE id = ?", (student_id,))
    db.commit()