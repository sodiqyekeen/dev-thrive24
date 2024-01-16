from db import *
from skillbridge.models.skill_exchange_model import *

def get_all_skill_exchanges():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM Skill_Exchange")
    Skill_Exchanges_data = cur.fetchall()
    Skill_Exchanges = []
    for Skill_Exchange_data in Skill_Exchanges_data:
        Skill_Exch = Skill_Exchange(Skill_Exchange_data['id'], Skill_Exchange_data['student1_ID'], Skill_Exchange_data['student2_ID'], Skill_Exchange_data['Skill_ID'], Skill_Exchange_data['Status']) 
        Skill_Exchanges.append(Skill_Exch)
    return Skill_Exchanges

def get_Skill_Exchange_by_id(Skill_Exchange_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM Skill_Exchange WHERE id = ?", (Skill_Exchange_id,))
    Skill_Exchange_data = cur.fetchone()
    if Skill_Exchange_data is None:
        return None
    Skill_Exch = Skill_Exchange(Skill_Exchange_data['id'], Skill_Exchange_data['student1_ID'], Skill_Exchange_data['student2_ID'], Skill_Exchange_data['Skill_ID'], Skill_Exchange_data['Status']) 
    return Skill_Exch

def add_new_Skill_Exchange(id, student1_ID, student2_ID, skill_ID, Satatus):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO Skill_Exchange (id, student1_ID, student2_ID, skill_ID, Satatus) VALUES (?,?,?,?,?)", (id, student1_ID, student2_ID, skill_ID, Satatus))
    db.commit()
    return cur.lastrowid

def Skill_Exchange_exists(student1_ID, student2_ID):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM Skill_Exchange WHERE student1_ID = ?, student2_ID = ?", (student1_ID, student2_ID))
    Skill_Exchange_data = cur.fetchone()
    if Skill_Exchange_data is None:
        return False
    return True

def update_Skill_Exchange(Skill_Exch : Skill_Exchange):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE Skill_Exchange SET student1_ID = ?, student2_ID = ?, skill_ID = ?, Satatus = ?  WHERE id = ?", (Skill_Exch.get_student1_ID(), Skill_Exch.get_student2_ID(), Skill_Exch.get_skill_ID(), Skill_Exch.get_Status(), Skill_Exch.get_id()))
    db.commit()

def delete_Skill_Exchange(Skill_Exchange_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM Skill_Exchange WHERE id = ?", (Skill_Exchange_id,))
    db.commit()
