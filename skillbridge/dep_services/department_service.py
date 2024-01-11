from db import *
from skillbridge.dep_models.department_model import *

def get_all_department():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM department")
    department_data = cur.fetchall()
    department = []
    for department_data in department_data:
        department = Department(department_data['id'], department_data['name'], department_data['faculty_id']) 
        department.append(department)
    return department

def get_department_by_id(department_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM department WHERE id = ?", (department_id,))
    department_data = cur.fetchone()
    if department_data is None:
        return None
    department = Department(department_data['id'], department_data['name'])
    return department

def add_new_department(department_name):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO department (name) VALUES (?)", (department_name,))
    db.commit()
    return cur.lastrowid

def department_exists(department_name):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM department WHERE name = ?", (department_name,))
    department_data = cur.fetchone()
    if department_data is None:
        return False
    return True

def update_department(department : Department):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE department SET name = ? WHERE id = ?", (department.get_name(), department.get_id()))
    db.commit()

def delete_department(department_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM department WHERE id = ?", (department_id,))
    db.commit()