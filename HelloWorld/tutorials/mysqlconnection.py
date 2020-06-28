import mysql.connector

my_db = mysql.connector.connect(host="localhost", user="root", passwd="password", database="sawan")
my_cursor = my_db.cursor()
my_cursor.execute('show databases')
for i in my_cursor:
    print(i)
print('\n')


my_cursor.execute('select * from sawan1')
result = my_cursor.fetchall()
for i in result:
    print(i)

