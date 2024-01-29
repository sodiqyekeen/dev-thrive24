from db import *
from models import USER_ROLE
from models.user_role_model import *

def get_all_users_role():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM department")
    users_role_data = cur.fetchall()
    users_role = []
    for user_role_data in users_role_data:
        user_role = USER_ROLE(user_role_data['id'], user_role_data['role_name']) 
        users_role.append(user_role)
    return users_role

def get_user_role_by_id(user_role_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM user_role WHERE id = ?", (user_role_id,))
    user_role_data = cur.fetchone()
    if user_role_data is None:
        return None
    user_role = USER_ROLE(user_role_data['id'], user_role_data['role_name'])
    return user_role

def add_new_user_role(user_role_name):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO user_role (role_name) VALUES (?)", (user_role_name,))
    db.commit()
    return cur.lastrowid

def user_role_exists(user_role_id, role_name):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM user_role WHERE id=?, role_name=?", (user_role_id, role_name))
    user_role_data = cur.fetchone()
    if user_role_data is None:
        return False
    return True

def update_user_role(user_role: USER_ROLE):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE user_role SET role_name = ? WHERE id = ?", (user_role.get_role_name(), user_role.get_id()))
    db.commit()

def delete_user_role(user_role_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM user_role WHERE id = ?", (user_role_id,))
    db.commit()