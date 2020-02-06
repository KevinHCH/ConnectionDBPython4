import psycopg2
import psycopg2.extras
from pprint import pprint

connection = psycopg2.connect(user = "postgres",
                              password = "1234",
                              host = "127.0.0.1",
                              port = "5432",
                              database = "postgres")

cur = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)#Devuelve array de datos, PERO permite acceder por nombre (Array assoc de php)
# cur = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)#Devuelve OBJ ReadlDict, que es un array de tuplas 
qSelect = "SELECT * FROM users"
cur.execute(qSelect)
results = cur.fetchall()

pprint(results)
pprint(results[0]['id'])

for user in results:
  print(user['name'] + '-->'+str(user['salary']) + '$')