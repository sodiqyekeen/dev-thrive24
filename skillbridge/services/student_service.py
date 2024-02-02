from db import *
from models.student_model import *

def get_all_students():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM student")
    students_data = cur.fetchall()
    students = []
    for student_data in students_data:
        student = Student(student_data['id'], student_data['matric_no'], student_data['first_name'], student_data['last_name'],
                          student_data['department_id'], student_data['level'], student_data['username'], student_data['password'], student_data['email']) 
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
                          student_data['department_id'], student_data['level'], student_data['username'], student_data['password'], student_data['email'])
    return student

def add_new_student(matric_no, first_name, last_name, department_id, level, username, password, email):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO student (matric_no, first_name, last_name, department_id, level, username, password, email) VALUES (?,?,?,?,?,?,?,?)", 
                (matric_no, first_name, last_name, department_id, level, username, password, email))
    db.commit()
    return cur.lastrowid

def student_exists(student_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM student WHERE id = ?", (student_id,))
    student_data = cur.fetchone()
    if student_data is None:
        return False
    return True

def update_student(student : Student):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE student SET matric_no = ?, first_name = ?, last_name = ?, department_id = ?, level = ?, username = ?, password = ?, email = ?  WHERE id = ?", 
                (student.get_matric_no(), student.get_first_name(), student.get_last_name(), student.get_department_id(), student.get_level(), student.get_username(),
                 student.get_password(), student.get_password(), student.get_email(), student.get_id()))
    db.commit()

def delete_student(student_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE * FROM student WHERE matric_no = ?", (student_id,))
    db.commit()
