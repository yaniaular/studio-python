#!/usr/bin/python
import psycopg2

conexion = psycopg2.connect(dbname="prueba", user="estudiante", password="estudiante")

cur = conexion.cursor()

cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

try:
    cur.execute("SELECT * FROM test;")
except Exception, e:
    pass

print cur.fetchall()

print cur.fetchone()

conexion.commit()

cur.close()
conexion.close()




