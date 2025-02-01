import sqlite3
from random import randint

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

age = 0
for i in range(1, 11):
    age += 10
    cursor.execute('''
    INSERT INTO Users (username, email, age, balance)
   VALUES (?, ?, ?, ?)
   ''', (f'User{i}', f'example{i}@gmail.com', age, 1000))

for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id=?', (i,))

cursor.execute('''
SELECT username, email, age, balance FROM Users 
Where age != 60''')

results = cursor.fetchall()
for res in results:
    print(f'Имя: {res[0]} | Почта: {res[1]} | {res[2]} | {res[3]}')


connection.commit()
connection.close()