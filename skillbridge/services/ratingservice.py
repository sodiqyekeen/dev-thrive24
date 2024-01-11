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
    rating = Rating(rating_data['id'], rating_data['tutor_id'], rating_data['user_id'], rating_data['rating'], rating_data['review'])
    return rating

def add_new_rating(tutor_id, user_id, rating, review):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO rating (tutor_id) VALUES (?)", (tutor_id,))
    cur.execute("INSERT INTO rating (user_id) VALUES (?)", (user_id,))
    cur.execute("INSERT INTO rating (rating) VALUES (?)", (rating,))
    cur.execute("INSERT INTO rating (review) VALUES (?)", (review,))
    db.commit()
    return cur.lastrowid

def rating_exists(tutor_id, user_id, rating, review):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM rating WHERE tutor_id = ?", (tutor_id,))
    cur.execute("SELECT * FROM rating WHERE user_id = ?", (user_id))
    cur.execute("SELECT * FROM rating WHERE rating = ?", (rating))
    cur.execute("SELECT * FROM rating WHERE review = ?", (review))
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
