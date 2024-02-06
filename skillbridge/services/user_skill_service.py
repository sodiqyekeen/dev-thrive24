from db import *
from models.user_skill_model import *


def get_all_User_Skills():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM User_Skill")
    User_Skills_data = cur.fetchall()
    User_Skills = []
    for User_Skill_data in User_Skills_data:
        user_skill = User_Skill(User_Skill_data['id'], User_Skill_data['Proficiency_level'], User_Skill_data['student_ID'], User_Skill_data['Skill_ID']) 
        User_Skills.append(user_skill)
    return User_Skills

def get_User_Skill_by_id(User_Skill_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM User_Skill WHERE id = ?", (User_Skill_id,))
    User_Skill_data = cur.fetchone()
    if User_Skill_data is None:
        return None
    user_skill = User_Skill(User_Skill_data['id'], User_Skill_data['Proficiency_level'], User_Skill_data['student_ID'], User_Skill_data['Skill_ID']) 
    return user_skill

def add_new_User_Skill(proficiency_level, student_ID, skill_ID):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO User_Skill (proficiency_level, student_ID, skill_ID) VALUES (?,?,?)", (proficiency_level, student_ID, skill_ID))
    db.commit()
    return cur.lastrowid

def User_Skill_exists(proficiency_level, student_ID, skill_ID):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM User_Skill WHERE proficiency_level = ?, student_ID = ?, skill_ID = ?", (proficiency_level, student_ID, skill_ID))
    User_Skill_data = cur.fetchone()
    if User_Skill_data is None:
        return False
    return True

def update_User_Skill(user_skill : User_Skill):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE User_Skill SET  proficiency_level = ?, student_ID = ?, skill_ID = ? WHERE id = ?", (user_skill.get_Proficiency_level(), user_skill.get_student_ID(), user_skill.get_Skill_ID(), user_skill.get_id()))
    db.commit()

def delete_User_Skill(User_Skill_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM User_Skill WHERE id = ?", (User_Skill_id,))
    db.commit()
