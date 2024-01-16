from db import *
from skillbridge.models.skills_model import *

def get_all_skill():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM skills")
    skills_data = cur.fetchall()
    skills = []
    for skill_data in skills_data:
        skill = skills(skill_data['id'], skill_data['Skill_Name'], skill_data['Description']) 
        skills.append(skill)
    return skills

def get_skills_by_id(skill_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM skills WHERE id = ?", (skill_id,))
    skill_data = cur.fetchone()
    if skill_data is None:
        return None
    skill = skill(skill_data['id'], skill_data['Skill_Name'])
    return skill

def add_new_skill(skill_name):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO skills (Skill_Name) VALUES (?)", (skill_name,))
    db.commit()
    return cur.lastrowid

def skill_exists(skill_name):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM skills WHERE Skill_Name = ?", (skill_name,))
    skill_data = cur.fetchone()
    if skill_data is None:
        return False
    return True

def update_skills(skill : Skills):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE skills SET Skill_Name = ?, Description = ? WHERE id = ?", (skill.get_name(), skill.get_Description(), skill.get_id()))
    db.commit()

def delete_skill(skill_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM skills WHERE id = ?", (skill_id,))
    db.commit()
