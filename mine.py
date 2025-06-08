from sqlite3 import *
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зарееструвати студента на курс")
    print("6. Показати студентів на конкретному курсі ")
    print("7. Вийти")

    choise = input("Оберіть опцію (1-7):")

    if choise == "1":
        name = input("Ім'я студента: ")
        age = int(input("Вік студента: ")) 
        cursor.execute("INSERT INTO students (name,age) VALUES (?,?)",(name,age))
        conn.commit()
        
        print("Студента успішно додано")

    if choise == "2":
        course_name = input("Назва курсу: ")
        instructor = input("Викладач: ")
        cursor.execute("INSERT INTO courses (course_name,instructor) VALUES (?,?)",(course_name,instructor))
        conn.commit()

        print("Курс успішно додано")

    if choise == "3":
        cursor.execute("SELECT name,age FROM students")
        for name,age in cursor.fetchall():
            print(f"Ім'я: {name}, Вік: {age}")

    if choise == "4":
        cursor.execute("SELECT course_name,instructor FROM courses")
        for course_name,instructor in cursor.fetchall():
            print(f"Курс: {course_name}, Викладач: {instructor}")

    if choise == "5":
        student_name = input("Ім'я студента якого треба записати на курс: ")
        cursor.execute("SELECT id FROM students WHERE name = ?", (student_name,))
        examination_name = cursor.fetchone()
        if not examination_name:
            print("Такого студента немає ")
            continue
        student_id = examination_name[0]

        course_name = input("Назва курсу: ")
        cursor.execute("SELECT course_id FROM courses WHERE course_name = ?", (course_name,))
        examination_course = cursor.fetchone()
        if not examination_course:
            print("Такого курсу немає ")
            continue
        course_id = examination_course[0]

        cursor.execute("INSERT INTO all_info (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
        conn.commit()
        print("Студент зареєстрований на курс")




    if choise == "6":
        course_name = input("Назва курсу: ")
        cursor.execute("""
            SELECT students.name, students.age FROM all_info
            JOIN students ON all_info.student_id = students.id
            JOIN courses ON all_info.course_id = courses.course_id
            WHERE courses.course_name = ?""", (course_name,))

        
        students_on_course = cursor.fetchall()
        
        if students_on_course:
            print(f"Студенти, зареєстровані на курс '{course_name}':")
            for student in students_on_course:
                print(f"Ім’я: {student[0]}, Вік: {student[1]}")
        else:
            print("На цьому курсі ще немає студентів або курс не знайдено.")


    if choise == "7":
        conn.close()
        break
    
    else:
        print("будь ласка, введіть число від 1 до 7.")