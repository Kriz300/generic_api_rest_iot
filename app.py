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
        posts = conn.execute('UPDATE Company SET company_name = ? WHERE company_api_key = ?', (name,api_key)).fetchall()
        conn.commit()
        conn.close()
        return str("updated"), 200
    elif request.method == 'DELETE':
        api_key  = request.args.get('company_api_key', None)
        posts = conn.execute('DELETE FROM Company WHERE Company_api_key=?', (api_key,)).fetchall()
        conn.commit()
        conn.close()
        return str("deleted"), 200

@app.route('/api/v1/location/', methods=["GET","POST","PUT","DELETE"])
def location():
    conn = get_db_connection()
    if request.method == 'GET':
        company_api_key  = request.args.get('company_api_key', None)
        if company_api_key  == "all":
            posts = conn.execute('SELECT * FROM location').fetchall()
        else:
            posts = conn.execute('SELECT * FROM location, company WHERE company.company_api_key = ? and location.company_ID = company.company_ID', (company_api_key,)).fetchone()
        conn.close()
        return str(posts), 200
    elif request.method == 'PUT':
        name  = request.form.get('name', None)
        api_key  = request.form.get('company_api_key', None)
        posts = conn.execute('UPDATE location SET location_name = ? WHERE company.company_id= ? and location.company_ID = company.company_ID', (name,api_key)).fetchall()
        conn.commit()
        conn.close()
        return str("updated"), 200
    elif request.method == 'POST':
        api_key  = request.form.get('company_api_key', None)
        company_id  = request.form.get('name', None)
        location_name  = request.form.get('name', None)
        location_country  = request.form.get('company_api_key', None)
        location_city  = request.form.get('name', None)
        location_meta = request.form.get('name', None)
        company_api_key = conn.execute('SELECT company_api_key FROM Company WHERE company_api_key= ?', (company_id,)).fetchone()#Lista
        if company_api_key[0] == api_key:
            posts = conn.execute('INSERT INTO location (company_ID, location_name,location_country, location_city, location_meta) VALUES (?,?,?,?,?)', (company_id,location_name,location_country,location_city,location_meta)).fetchall()
            conn.commit()
            conn.close()
            return str("created"), 201
        else:
            return str("bad request"), 400
    elif request.method == 'DELETE':
        company_api_key  = request.args.get('key', None)
        posts = conn.execute('DELETE FROM location,company WHERE Company_id=?', (key,)).fetchall()
        conn.commit()
        conn.close()
        return str("deleted"), 200
    elif request.method == 'DELETE':
        api_key  = request.args.get('company_api_key', None)
        posts = conn.execute('DELETE FROM Company WHERE Company_api_key=?', (api_key,)).fetchall()
        conn.commit()
        conn.close()
        return str("deleted"), 200
    conn.close()
    return str(posts), 200

@app.route('/api/v1/sensor/', methods=["GET","POST","PUT","DELETE"])
def sensor():
    conn = get_db_connection()
    if request.method == 'GET':
        company_api_key  = request.args.get('company_api_key', None)
        if company_api_key == "all":
            posts = conn.execute('SELECT * FROM Sensor s, Company c, location l WHERE s.location_ID = l.location_ID and l.company_ID = c.company_ID and c.company_api_key= ?', (company_api_key,)).fetchall()#Lista
        else:
            company_api_key  = request.args.get('sensor_api_key', None)
            posts = conn.execute('SELECT * FROM Sensor s, Company c, location l WHERE s.sensor_api_key = ? and s.location_ID = l.location_ID and l.company_ID = c.company_ID and c.company_api_key= ?', (company_api_key,)).fetchone()#Lista
        conn.close()
        return str(posts), 200
    elif request.method == 'POST':
        location_ID = request.args.get('location_ID', None)
        sensor_name = request.form.get('sensor_name', None)
        sensor_category = request.form.get('sensor_category', None)
        sensor_meta = request.form.get('sensor_meta', None)
        sensor_api_key = request.form.get('sensor_api_key', None)
        posts = conn.execute('INSERT INTO Sensor (location_ID, sensor_name, sensor_category, sensor_meta, sensor_api_key) VALUES (?, ?, ?, ?, ?)', (location_ID, sensor_name, sensor_category, sensor_meta, sensor_api_key)).fetchall()
        conn.commit()
        conn.close()
        return str("created"), 201
    elif request.method == 'PUT':
        sensor_name = request.form.get('sensor_name', None)
        sensor_api_key = request.form.get('sensor_api_key', None)
        posts = conn.execute('UPDATE Sensor SET sensor_name = ? WHERE sensor_api_key = ?', (sensor_name,sensor_api_key)).fetchall()
        conn.commit()
        conn.close()
        return str("updated"), 200
    elif request.method == 'DELETE':
        sensor_api_key = request.form.get('sensor_api_key', None)
        posts = conn.execute('DELETE FROM Sensor WHERE sensor_api_key=?', (sensor_api_key,)).fetchall()
        conn.commit()
        conn.close()
        return str("deleted"), 200
    conn.close()
    return str(posts), 200

@app.route('/api/v1/sensor_data/', methods=["POST","GET"])
def sensor_data():
    var  = request.args.get('var', None)
    api_key = var['sensor_api_key']
    conn = get_db_connection()
    if request.method == 'POST':
        api_key_server = conn.execute('SELECT * FROM Sensor WHERE sensor_api_key =?', (api_key,)).fetchall()
        if api_key_server == None:
            conn.close()
            return 'Failed: Not matched api_key, try again', 400
        else:
            posts = conn.execute('INSERT INTO Sensor_Data(ID_sensor,Data) VALUES(?)', (var['data'],)).fetchall()
            conn.close()
            return 'created', 201
    elif request.method == 'GET':
        server_company_api_key = conn.execute('SELECT * FROM Sensor WHERE sensor_api_key =?' + (api_key,)).fetchall()
        if server_company_api_key == var['company_api_key']:
            conn.close()
            return str(posts), 201
        else:
            conn.close()
            return 400
    conn.close()
    return 'raro',400

    conn = get_db_connection()
    if request.method == 'GET':
        company_api_key  = request.args.get('company_api_key', None)
        if company_api_key == "all":
            posts = conn.execute('SELECT * FROM Company').fetchall()#Lista
        else:
            posts = conn.execute('SELECT * FROM Company WHERE company_api_key= ?', (company_api_key,)).fetchone()#Lista
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
        posts = conn.execute('UPDATE Company SET company_name = ? WHERE company_api_key = ?', (name,api_key)).fetchall()
        conn.commit()
        conn.close()
        return str("updated"), 200
    elif request.method == 'DELETE':
        api_key  = request.args.get('company_api_key', None)
        posts = conn.execute('DELETE FROM Company WHERE Company_api_key=?', (api_key,)).fetchall()
        conn.commit()
        conn.close()
        return str("deleted"), 200
    conn.close()
    return str(posts), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)