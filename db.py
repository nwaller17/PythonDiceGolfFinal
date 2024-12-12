import sqlite3 # Used https://docs.python.org/3/library/sqlite3.html for syntax help

def create_database():
    conn = sqlite3.connect('final.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professional_golfers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_pro_scores():
    conn = sqlite3.connect('final.db')
    cursor = conn.cursor()

    golfers = [
        ('Phil Mickelson', 34),
        ('Rory McIlroy', 35),
        ('John Daly', 42),
        ('Jordan Spieth', 33),
        ('Tiger Woods', 31),
    ]

    for golfer in golfers:
        cursor.execute("SELECT * FROM professional_golfers WHERE name = ?", (golfer[0],))
        if not cursor.fetchone():
            cursor.execute('INSERT INTO professional_golfers (name, score) VALUES (?, ?)', golfer)  
    conn.commit()
    conn.close()

def display_scores():
    conn = sqlite3.connect('final.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, score FROM professional_golfers")
    scores = cursor.fetchall()
    print("\nProfessional Golfers Scores:")
    if scores:
        for name, score in scores:
            print(f"{name}: {score} strokes")
    else:
        print("No scores available.")
    conn.close()

create_database()
insert_pro_scores()
