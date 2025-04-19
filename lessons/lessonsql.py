import sqlite3
connect = sqlite3.connect('marvel_not_normal.db')
cursor = connect.cursor()
cursor.execute('select+from MarvelCharacters')
