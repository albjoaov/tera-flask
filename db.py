import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

pw = os.environ["PASS"]
u = os.environ["DB_USER"]
j = os.environ["HOST"]
print("aaaaa", u)
print("bbbbb", j)
print("ccccc", pw)

connection = psycopg2.connect(dbname="teste1", user="postgress", host="localhost", password="postgres")
cursor = connection.cursor()
cursor.execute("CREATE TABLE test(id serial PRIMARY KEY, name varchar, email varchar)")
connection.commit()
cursor.close()
cursor.close()

# cur.execute("SELECT * FROM test")
# items = cur.fetchall()