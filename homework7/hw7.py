import sqlite3 as sq

with sq.connect('students.db') as conn:
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30),
        surname VARCHAR(30),
        hobby VARCHAR(50),
        year INTEGER,
        hw_points INTEGER
    )''')

    students_data = [
        ('umar', 'umarov', 'tennis', 2007, 5),
        ('akinov','umarov', 'tennis', 2002, 2),
        ('nurlan', 'nurgazaliev', 'tennis', 2001, 2),
        ('bektur', 'akinov', 'tennis', 2001, 2),
        ('nurlan', 'akinov', 'tennis', 2007, 4),
        ('umar', 'abdyrazakov', 'tennis', 2003, 1),
        ('umar', 'nurlanov', 'tennis', 2007, 3),
        ('bektur', 'abdrahmanovich', 'tennis', 2001, 2),
        ('bektur', 'nurlanov', 'tennis', 2001, 4)
    ]

    cur.executemany('''INSERT INTO students (name, surname, hobby, year, hw_points)
                       VALUES (?, ?, ?, ?, ?)''', students_data)

    cur.execute('''SELECT * FROM students WHERE LENGTH(surname) > 10''')
    print("Students with surname longer than 10 characters:")
    for row in cur.fetchall():
        print(row)

    cur.execute('''UPDATE students SET name = 'genius' WHERE hw_points > 4''')


    cur.execute('''SELECT * FROM students WHERE name = 'genius' ''')
    print("\nStudents with 'genius' as their name:")
    for row in cur.fetchall():
        print(row)

    cur.execute('''DELETE FROM students WHERE id % 2 = 0''')