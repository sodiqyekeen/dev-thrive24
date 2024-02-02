from db import *
from models.project_model import *

def get_all_projects():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM project")
    projects_data = cur.fetchall()
    projects = []
    for project_data in projects_data:
        project = Project(project_data['id'], project_data['project_title'], project_data['project_description'], project_data['project_status']) 
        projects.append(project)
    return projects

def get_project_by_id(project_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM project WHERE id = ?", (project_id,))
    project_data = cur.fetchone()
    if project_data is None:
        return None
    project = Project(project_data['id'], project_data['project_title'], project_data['project_description'], project_data['project_status'])
    return project

def add_new_project(project_title, project_description, project_status):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO project (project_title, project_description, project_status) VALUES (? ,?, ?)", (project_title, project_description, project_status))
    db.commit()
    return cur.lastrowid

def project_exists(project_title, project_description, project_status):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM project WHERE project_title = ?, project_description = ?, project_status = ?", (project_title, project_description, project_status))
    project_data = cur.fetchone()
    if project_data is None:
        return False
    return True

def update_rating(project : Project):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE project SET project_title = ?, project_description = ?, project_status = ? WHERE id = ?", (project.get_project_title(), project.get_project_description(), project.get_project_status(), project.get_id()))
    db.commit()

def delete_project(project_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM project WHERE id = ?", (project_id,))
    db.commit()