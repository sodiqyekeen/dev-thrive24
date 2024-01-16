from db import *
from skillbridge.models.rating import *

def get_all_rating():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM rating")
    rating_data = cur.fetchall()
    rating = []
    for rating_data in rating_data:
        rating = Rating(rating_data['id'], rating_data['tutor_id'], rating_data['user_id'], rating_data['rating'], rating_data['review']) 
        rating.append(rating)
    return rating

def get_rating_by_id(rating_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM rating WHERE id = ?", (rating_id,))
    rating_data = cur.fetchone()
    if rating_data is None:
        return None
    rating = Rating(rating_data['id'], rating_data['name'])
    return rating

def add_new_rating(rating_name):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO rating (name) VALUES (?)", (rating_name,))
    db.commit()
    return cur.lastrowid

def rating_exists(rating_name):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM rating WHERE name = ?", (rating_name,))
    rating_data = cur.fetchone()
    if rating_data is None:
        return False
    return True

def update_rating(rating : Rating):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE rating SET name = ? WHERE id = ?", (rating.get_name(), rating.get_id()))
    db.commit()

def delete_rating(rating_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM rating WHERE id = ?", (rating_id,))
    db.commit()
