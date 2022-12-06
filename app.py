from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('Backbone.db')
    return conn

@app.route('/api/v1/company/', methods=["GET","POST", "PUT","DELETE"])
def company():
    conn = get_db_connection()
    if request.method == 'GET':
        company_api_key  = request.args.get('company_api_key', None)
        if company_api_key == "all":
            posts = conn.execute('SELECT * FROM Company').fetchall()#Lista
        else:
            posts = conn.execute('SELECT * FROM Company WHERE company_api_key= ?', (company_api_key,)).fetchone()#Lista
        conn.close()
        return str(posts), 200
    elif request.method == 'POST':
        name  = request.form.get('name', None)
        api_key  = request.form.get('company_api_key', None)
        posts = conn.execute('INSERT INTO Company (company_name, company_api_key) VALUES (?,?)', (name,api_key)).fetchall()
        conn.commit()
        conn.close()
        return str("created"), 201
    elif request.method == 'PUT':
        name  = request.form.get('name', None)
        api_key  = request.form.get('company_api_key', None)
        posts = conn.execute('UPDATE company SET company_name = ? WHERE company_api_key = ?', (name,api_key)).fetchall()
        conn.commit()
        conn.close()
        return str("updated"), 200
    elif request.method == 'DELETE':
        api_key  = request.args.get('company_api_key', None)
        posts = conn.execute('DELETE FROM company WHERE company_api_key=?', (api_key,)).fetchall()
        conn.commit()
        conn.close()
        return str("deleted"), 200

@app.route('/api/v1/location/', methods=["GET","POST","PUT","DELETE"])
def location():
    conn = get_db_connection()
    if request.method == 'GET':
        company_api_key  = request.args.get('company_api_key', None)
        location_id = request.args.get('location_id', None)
        if location_id  == "all":
            posts = conn.execute('SELECT location.location_ID, location.company_ID, location.location_name, location.location_country, location.location_city, location.location_meta FROM location, company where location.company_ID = company.company_ID and company.company_api_key = ?', (company_api_key,)).fetchall()
        else:
            posts = conn.execute('SELECT location.location_ID, location.company_ID, location.location_name, location.location_country, location.location_city, location.location_meta FROM location, company WHERE company.company_api_key = ? and company.company_ID = location.company_ID and location.location_ID = ?', (company_api_key,location_id)).fetchone()
        conn.close()
        return str(posts), 200
    elif request.method == 'PUT':
        location_name  = request.form.get('location_name', None)
        location_id = request.form.get('location_id', None)
        api_key  = request.form.get('company_api_key', None) 
        posts = conn.execute('UPDATE location SET location_name = ? FROM company WHERE company.company_api_key = ? and location.company_ID = company.company_ID and location.location_ID = ?', (location_name, location_id,api_key)).fetchall()
        conn.commit()
        conn.close()
        return str("updated"), 200
    elif request.method == 'POST':
        api_key  = request.form.get('company_api_key', None)
        company_id  = request.form.get('company_id', None)
        location_name  = request.form.get('location_name', None)
        location_country  = request.form.get('location_country', None)
        location_city  = request.form.get('location_city', None)
        location_meta = request.form.get('location_meta', None)
        company_api_key = conn.execute('SELECT company_api_key FROM Company WHERE company_ID= ?', (company_id,)).fetchone()#Lista
        if company_api_key[0] == api_key:
            posts = conn.execute('INSERT INTO location (company_ID, location_name,location_country, location_city, location_meta) VALUES (?,?,?,?,?)', (company_id,location_name,location_country,location_city,location_meta)).fetchall()
            conn.commit()
            conn.close()
            return str("created"), 201
        else:
            return str("bad request"), 400
    elif request.method == 'DELETE':
        company_api_key  = request.args.get('company_api_key', None)
        location_id  = request.args.get('location_id', None)
        posts = conn.execute('DELETE FROM location WHERE EXISTS (SELECT * FROM company WHERE company.company_api_key = ? and location.company_ID = company.company_ID and location.location_ID = ?)', (company_api_key,location_id)).fetchall()
        conn.commit()
        conn.close()
        return str("deleted"), 200

@app.route('/api/v1/sensor/', methods=["GET","POST","PUT","DELETE"])
def sensor():
    conn = get_db_connection()
    if request.method == 'GET':
        company_api_key  = request.args.get('company_api_key', None)
        sensor_api_key = request.args.get('sensor_api_key', None)
        if sensor_api_key == "all":
            posts = conn.execute('SELECT s.location_ID, s.sensor_ID, s.sensor_name, s.sensor_category, s.sensor_meta, s.sensor_api_key FROM Sensor s, Company c, location l WHERE s.location_ID = l.location_ID and l.company_ID = c.company_ID and c.company_api_key= ?', (company_api_key,)).fetchall()#Lista
        else:
            posts = conn.execute('SELECT s.location_ID, s.sensor_ID, s.sensor_name, s.sensor_category, s.sensor_meta, s.sensor_api_key FROM Sensor s, Company c, location l WHERE s.sensor_api_key = ? and s.location_ID = l.location_ID and l.company_ID = c.company_ID and c.company_api_key= ?', (sensor_api_key, company_api_key)).fetchone()#Lista
        conn.close()
        return str(posts), 200
    elif request.method == 'POST':
        api_key  = request.form.get('company_api_key', None)
        location_id = request.form.get('location_id', None) #del sensor
        sensor_name = request.form.get('sensor_name', None)
        sensor_category = request.form.get('sensor_category', None)
        sensor_meta = request.form.get('sensor_meta', None)
        sensor_api_key = request.form.get('sensor_api_key', None)
        company_api_key = conn.execute('SELECT company.company_api_key FROM location, Company WHERE location.location_ID= ? and location.company_ID = company.company_ID', (location_id,)).fetchone()#Lista
        if company_api_key[0] == api_key:
            posts = conn.execute('INSERT INTO Sensor (location_ID, sensor_name, sensor_category, sensor_meta, sensor_api_key) VALUES (?, ?, ?, ?, ?)', (location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key)).fetchall()
            conn.commit()
            conn.close()
            return str("created"), 201
        else:
            return str("bad request"), 400
    elif request.method == 'PUT':
        sensor_name = request.form.get('sensor_name', None)
        sensor_api_key = request.form.get('sensor_api_key', None)
        api_key  = request.form.get('company_api_key', None)
        posts = conn.execute('UPDATE Sensor SET sensor_name = ? FROM location, company WHERE sensor_api_key = ? and sensor.location_ID = location.location_ID and location.company_ID = company.company_ID and company.company_api_key = ?', (sensor_name, sensor_api_key, api_key)).fetchall()
        conn.commit()
        conn.close()
        return str("updated"), 200
    elif request.method == 'DELETE':
        sensor_api_key = request.args.get('sensor_api_key', None)
        api_key  = request.args.get('company_api_key', None)
        posts = conn.execute('DELETE FROM Sensor WHERE EXISTS (SELECT * FROM location, company WHERE sensor_api_key = ? and sensor.location_ID = location.location_ID and location.company_ID = company.company_ID and company.company_api_key = ?)', (sensor_api_key, api_key)).fetchall()
        conn.commit()
        conn.close()
        return str("deleted"), 200
    conn.close()
    return str(posts), 200

@app.route('/api/v1/sensor_data/', methods=["POST","GET"])
def sensor_data():
    conn = get_db_connection()
    if request.method == 'POST':
        data = request.form.get('data', None)
        sensor_api_key = request.form.get('sensor_api_key', None)
        sensor_id = conn.execute('SELECT sensor.sensor_ID FROM Sensor WHERE sensor.sensor_api_key = ?', (sensor_api_key,)).fetchone()#Lista
        posts = conn.execute('INSERT INTO Sensor_data (sensor_ID, data, time) VALUES (?, ?, ?)', (sensor_id,data['data'], data['time'])).fetchall()
        conn.commit()
        conn.close()
        return 'created', 201
    elif request.method == 'GET':
        sensor_id = conn.execute('SELECT sensor_ID FROM Sensor WHERE sensor_api_key =?' + (sensor_api_key,)).fetchall()
        posts = conn.execute('SELECT * FROM sensor_data WHERE sensor_ID = ?', (sensor_id,)).fetchall()
        conn.close()
        return str(posts), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)