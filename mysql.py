import pymysql
import pymysql.cursors
from pprint import pprint

db = pymysql.connect(host='localhost',
                      user='root',
                      password='4321',
                      db='test',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)


cursor = db.cursor()
cursor.execute("insert into test (name) values ('jimmy'), ('John'), ('Jamie');")

cursor.execute("select * from test;")
data = cursor.fetchall()
print(data)
# for person in data:
#   print(person['id'])


cursor.close()
db.commit() #Es importante cerrar la conexion para insertar los datos