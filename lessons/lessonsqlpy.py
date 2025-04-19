import sqlite3

DDL_SCRIPT = 'lessons\lesson_40.sql'
DATA_BASE = 'students_new.db'

connection = sqlite3.connect(DATA_BASE)

cursor = connection.cursor()

#sql_file = 'lessons\lesson_40.sql'

#with open(DDL_SCRIPT, 'r', encoding='utf-8') as file:
#    sql_script = file.read()

#cursor.executescript(sql_script)
SELECT_QUERY_1 = "SELECT * FROM subjects"
SELECT_QUERY_2 = """
SELECT st.first_name, st.last_name, st.age, gr.group_name
FROM students st
LEFT JOIN groups gr ON st.group_id = gr.id
"""
SELECT_QUERY = "SELECT * FROM students"

all_students = cursor.execute(SELECT_QUERY_2).fetchall()
print(type(all_students))
print(all_students)

connection.commit()
connection.close()