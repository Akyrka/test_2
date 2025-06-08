import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Таблиця студентів
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20),
        age INTEGER,
        major VARCHAR(20)
    );
""")

# Таблиця курсів
cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name VARCHAR(20),
        instructor VARCHAR(20)
    );
""")

# Таблиця для зв’язку студентів і курсів 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS all_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    );
""")

conn.commit()
conn.close()
