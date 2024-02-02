from db import *
from models.department_model import *

def get_all_departments():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM department")
    departments_data = cur.fetchall()
    departments = []
    for department_data in departments_data:
        department = Department(department_data['id'], department_data['name'], department_data['faculty_id']) 
        departments.append(department)
    return departments

def get_department_by_id(department_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM department WHERE id = ?", (department_id,))
    department_data = cur.fetchone()
    if department_data is None:
        return None
    department = Department(department_data['id'], department_data['name'], department_data['faculty_id'])
    return department

def add_new_department(department_name, faculty_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO department (name) AND department (faculty_id) VALUES (?)", (department_name, faculty_id))
    db.commit()
    return cur.lastrowid

def department_exists(department_name, faculty_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM department WHERE name = ?, faculty_id = ?", (department_name, faculty_id))
    department_data = cur.fetchone()
    if department_data is None:
        return False
    return True

def update_department(department : Department):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE department SET name = ?, faculty_id = ? WHERE id = ?", (department.get_name(), department.get_faculty_id(), department.get_id()))
    db.commit()

def delete_department(department_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM department WHERE id = ?", (department_id,))
    db.commit()