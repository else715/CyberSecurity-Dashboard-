import sqlite3

def get_db_connection():
    conn = sqlite3.connect('security.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_logs():
    conn = get_db_connection()
    logs = conn.execute('SELECT * FROM logs').fetchall()
    conn.close()
    return [dict(row) for row in logs]

def get_threats():
    conn = get_db_connection()
    threats = conn.execute('SELECT * FROM threats').fetchall()
    conn.close()
    return [dict(row) for row in threats]
