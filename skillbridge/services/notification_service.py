from db import *
from skillbridge.models.notification_model import *

def get_all_notification():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM notification")
    notification_data = cur.fetchall()
    notification = []
    for notification_data in notification_data:
        notification = notification(notification_data['id'],notification_data['user_id'],notification_data['content'] ) 
        notification.append(notification)
    return notification

def get_notification_by_id(notification_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM notification WHERE id = ?", (notification_id,))
    notification_data = cur.fetchone()
    if notification_data is None:
        return None
    notification = Notification(notification_data['id'], notification_data['user_id'], notification_data['user_id'], notification_data['content'])
    return notification

def add_new_notification(id, user_id,content):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO notification (id, user_id, content) VALUES (?)", (id, user_id,content))
    db.commit()
    return cur.lastrowid

def notification_exists(id,user_id,content ):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM notification WHERE id, user_id, AND content = ?", (id, user_id, content))
    notification_data = cur.fetchone()
    if notification_data is None:
        return False
    return True

def update_notification(notification : Notification):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE notification SET name = ? WHERE id = ?", (notification.get_id()))
    db.commit()

def delete_notification(notification_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM notification WHERE id = ?", (notification_id,))
    db.commit()
