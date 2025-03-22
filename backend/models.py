import sqlite3

conn = sqlite3.connect('security.db')
cursor = conn.cursor()

# Create Logs Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        source_ip TEXT,
        severity TEXT,
        message TEXT
    )
''')

# Create Threats Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS threats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        description TEXT,
        risk_level TEXT
    )
''')

conn.commit()
conn.close()
