import sqlite3

conn = sqlite3.connect('Backbone.db')
cur = conn.cursor()

#Crea las tablas
'''
with open('schemes.sql') as f:
    conn.executescript(f.read())
'''

#Crea al Admin
cur.execute("INSERT INTO admin VALUES ('admin','pass')")

#Crea Company
cur.execute("INSERT INTO company VALUES (1,'prime','c_ssak_1')")

#Crea ubicaciones
cur.execute("INSERT INTO location VALUES (1,'local1','Chile','stgo','Robada 3 veces')")

#Crea sensores
cur.execute("INSERT INTO sensor VALUES (1,1,'sensor1','movimiento','Si te mueves te ve','s_ssak_1')")

conn.commit()
conn.close()

#Super
#Secret
#API
#Key