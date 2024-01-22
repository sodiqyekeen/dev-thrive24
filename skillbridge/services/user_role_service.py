from db import *
from skillbridge.models import user_role
from skillbridge.models.user_role_model import *

def get_all_user_role():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM department")
    user_role_data = cur.fetchall()
    user_role = []
    for user_role_data in user_role_data:
        user_role = user_role(user_role_data['id'], user_role_data['role_name']) 
        user_role.append(user_role)
    return user_role

def get_user_role_by_id(user_role_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM user_role WHERE id = ?", (user_role_id,))
    user_role_data = cur.fetchone()
    if user_role_data is None:
        return None
    user_role = user_role(user_role_data['id'], user_role_data['role_name'])
    return get_all_user_role

def add_new_user_role(user_role_id,user_role_role_name ):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO user_role (id) AND user_role (role) VALUES (?)", (user_role_id, user_role_role_name))
    db.commit()
    return cur.lastrowid

def user_role_exists(user_role_id, role_name):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM user_role WHERE id AND role_name = ?", (user_role_id, role_name))
    user_role_data = cur.fetchone()
    if user_role_data is None:
        return False
    return True

def update_user_role(user_role: role_name):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE department SET name = ? WHERE id = ?", (user_role.get_name(), user_role.get_role_name()))
    db.commit()

def delete_department(user_role_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM user_role WHERE id = ?", (user_role_id,))
    db.commit()