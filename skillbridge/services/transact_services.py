from skillbridge.db import *
from models.transact_model import *


def get_all_transactions():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM transact")
    transactions_data = cur.fetchall()
    transactions = []
    for transaction_data in transactions_data:
        transaction = Transact(transaction_data['id'], transaction_data['payment_reference'], transaction_data['payment_status']) 
        transactions.append(transaction)
    return transactions

def get_transaction_by_id(transaction_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM transact WHERE id = ?", (transaction_id,))
    transaction_data = cur.fetchone()
    if transaction_data is None:
        return None
    transaction = Transact(transaction_data['id'], transaction_data['payment_reference'], transaction_data['payment_status'])
    return transaction

def add_new_transaction(payment_reference):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO transact (payment_reference, payment_status) VALUES (?,?)", (payment_reference, 'paid', ))
    db.commit()
    return cur.lastrowid

def transaction_exists(payment_reference):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM faculty WHERE payment_reference = ?", (payment_reference,))
    transaction_data = cur.fetchone()
    if transaction_data is None:
        return False
    return True

def update_tranaction(transaction : Transact):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE transact SET payment_reference = ?, payment_status = ?,  WHERE id = ?", (transaction.get_payment_reference(), transaction.get_payment_status(), transaction.get_id()))
    db.commit()

def delete_transaction(transaction_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM transact WHERE id = ?", (transaction_id,))
    db.commit()