from db import *
from models.rating_model import *

def get_all_ratings():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM rating")
    ratings_data = cur.fetchall()
    ratings = []
    for rating_data in ratings_data:
        rating = Rating(rating_data['id'], rating_data['tutor_id'], rating_data['user_id'], rating_data['rating'], rating_data['review']) 
        ratings.append(rating)
    return ratings

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
    cur.execute("INSERT INTO rating (tutor_id, user_id, rating, review) VALUES (?, ?, ?, ?)", (tutor_id, user_id, rating, review))
    db.commit()
    return cur.lastrowid

def rating_exists(tutor_id, user_id, rating, review):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM rating WHERE tutor_id = ?, user_id = ?, rating = ?, review = ?", (tutor_id, user_id, rating, review))
    rating_data = cur.fetchone()
    if rating_data is None:
        return False
    return True

def update_rating(rating : Rating):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE rating SET  tutor_id = ?, user_id = ?, rating = ?, review = ? WHERE id = ?", (rating.get_tutor_id(), rating.get_user_id(), rating.get_rating(), rating.get_review, rating.get_id()))
    db.commit()

def delete_rating(rating_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM rating WHERE id = ?", (rating_id,))
    db.commit()
