import sqlite3

conn = sqlite3.connect('../Backbone.db')

#Crea las tablas
with open('schemes.sql') as f:
    conn.executescript(f.read())

#Crea al Admin
conn.execute("INSERT INTO Admin (username, password) VALUES ('admin','pass')")

#Crea Company
conn.execute("INSERT INTO Company (company_name, company_api_key) VALUES ('prime','c_ssak_1')")

#Crea ubicaciones
conn.execute("INSERT INTO Location (company_ID, location_name, location_country, location_city, location_meta) VALUES (1,'local1','Chile','stgo','Robada 3 veces')")

#Crea sensores
conn.execute("INSERT INTO Sensor (location_ID, sensor_name, sensor_category, sensor_meta, sensor_api_key) VALUES (1,'sensor1','movimiento','Si te mueves te ve','s_ssak_1')")

conn.commit()
conn.close()

#Super
#Secret
#API
#Key