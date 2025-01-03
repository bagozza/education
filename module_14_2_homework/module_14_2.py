import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

cursor.execute(' CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
# for num in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{num}", f"example{num}@gmail.com", num * 10, 1000))
# cursor.execute('UPDATE Users SET balance = ? WHERE id % 2', (500, ))
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age <> ?', (60,))
# cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users')
num_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
bal_users = cursor.fetchone()[0]
print(bal_users / num_users)
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]}, Почта: {user[1]}, Возраст:{user[2]}, Баланс:{user[3]}')
connection.commit()
connection.close()
