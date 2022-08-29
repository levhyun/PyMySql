import pymysql

db = pymysql.connect(host="localhost", user="root", password="123456", charset="utf8")

cursor = db.cursor()

cursor.execute('CREATE DATABASE manager;')

cursor.execute('USE manager;')

cursor.execute('CREATE TABLE member('
               'id INT(5) NOT NULL AUTO_INCREMENT,'
               'email VARCHAR(30) NOT NULL,'
               'password VARCHAR(16) NOT NULL,'
               'name VARCHAR(20) NOT NULL,'
               'age INT(5) NOT NULL,'
               'PRIMARY KEY(id)); ')

for i in range(5):
    cursor.execute('INSERT INTO member(email, password, name, age) '
                   'VALUES ("NONE@gmail.com", "NONE", "NONE", 0);')

db.commit()
db.close()