from db import *
from models.notification_model import *

def get_all_notifications():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM notification")
    notifications_data = cur.fetchall()
    notifications = []
    for notification_data in notifications_data:
        notification = Notification(notification_data['id'],notification_data['user_id'],notification_data['content'] ) 
        notifications.append(notification)
    return notifications

def get_notification_by_id(notification_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM notification WHERE id = ?", (notification_id,))
    notification_data = cur.fetchone()
    if notification_data is None:
        return None
    notification = Notification(notification_data['id'], notification_data['user_id'], notification_data['content'])
    return notification

def add_new_notification( user_id,content):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO notification (user_id, content) VALUES (?,?)", (user_id,content))
    db.commit()
    return cur.lastrowid

def notification_exists(user_id,content ):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM notification WHERE user_id =?, content = ?", ( user_id, content))
    notification_data = cur.fetchone()
    if notification_data is None:
        return False
    return True

def update_notification(notification : Notification):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE notification SET user_id = ?, content = ?, WHERE id = ?", (notification.get_user_id(), notification.get_content(), notification.get_id()))
    db.commit()

def delete_notification(notification_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM notification WHERE id = ?", (notification_id,))
    db.commit()
