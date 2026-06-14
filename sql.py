#This file maintains the database and is called by the Python script to get the data from the database and return it to the user.
import sqlite3

def create_connection():
    conn = sqlite3.connect('attendance.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_record(student_name, status):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO attendance (student_name, status)
        VALUES (?, ?)
    ''', (student_name, status))
    conn.commit()
    conn.close()

def fetch_records():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM attendance')
    records = cursor.fetchall()
    conn.close()
    return records
def delete_all_records():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM attendance')
    conn.commit()
    conn.close()