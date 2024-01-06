from db import *
from models import *

def get_all_faculties():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM faculty")
    faculties_data = cur.fetchall()
    faculties = []
    for faculty_data in faculties_data:
        faculty = Faculty(faculty_data['id'], faculty_data['name']) 
        faculties.append(faculty)
    return faculties

def get_faculty_by_id(faculty_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM faculty WHERE id = ?", (faculty_id,))
    faculty_data = cur.fetchone()
    if faculty_data is None:
        return None
    faculty = Faculty(faculty_data['id'], faculty_data['name'])
    return faculty

def add_new_faculty(faculty_name):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO faculty (name) VALUES (?)", (faculty_name,))
    db.commit()
    return cur.lastrowid

def faculty_exists(faculty_name):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM faculty WHERE name = ?", (faculty_name,))
    faculty_data = cur.fetchone()
    if faculty_data is None:
        return False
    return True

def update_faculty(faculty : Faculty):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE faculty SET name = ? WHERE id = ?", (faculty.get_name(), faculty.get_id()))
    db.commit()

def delete_faculty(faculty_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM faculty WHERE id = ?", (faculty_id,))
    db.commit()