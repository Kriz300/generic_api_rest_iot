from multiprocessing import connection
import sqlite3
from flask import Flask, request

'''
connect = sqlite3.connect("Backbone.db")
cursor = connect.cursor()
cursor.execute("CREATE TABLE Admin(Username TEXT NOT NULL, Password TEXT NOT NULL)")
cursor.execute("CREATE TABLE Company(ID INTEGER NOT NULL, Company_name TEXT NOT NULL, Company_api_key TEXT NOT NULL UNIQUE)")
cursor.execute("CREATE TABLE Location(Company_id INTEGER NOT NULL, Location_name TEXT NOT NULL, Location_country TEXT NOT NULL, Location_city TEXT NOT NULL, Location_meta TEXT NOT NULL)")
cursor.execute("CREATE TABLE Sensor(Location_id INTEGER NOT NULL, Sensor_id INTEGER NOT NULL, Sensor_name TEXT NOT NULL, Sensor_category TEXT NOT NULL, Sensor_meta TEXT NOT NULL, Sensor_api_key TEXT NOT NULL UNIQUE)")
cursor.execute("CREATE TABLE Sensor_Data(ID_sensor TEXT NOT NULL, Data TEXT NOT NULL)")
'''
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('Backbone.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/v1/company/', methods=["GET","PUT","DELETE"])
def company():
    var  = request.args.get('var', None)
    conn = get_db_connection()
    if request.method == 'GET':
        if var == "all":
            posts = conn.execute('SELECT * FROM Company').fetchall()
        else:
            posts = conn.execute('SELECT * FROM Company WHERE company_api_key=' + var).fetchall()
        conn.close()
    elif request.method == 'PUT':
        posts = conn.execute('SELECT * FROM Company WHERE company_api_key=' + var).fetchall()
    elif request.method == 'DELETE':
        posts = conn.execute('SELECT * FROM Company WHERE company_api_key=' + var).fetchall()
    return str(posts), 200

@app.route('/api/v1/location/', methods=["GET","PUT","DELETE"])
def location():
    var  = request.args.get('var', None)
    conn = get_db_connection()
    if request.method == 'GET':
        if var == "all":
            posts = conn.execute('SELECT * FROM Location').fetchall()
        else:
            posts = conn.execute('SELECT * FROM Location WHERE company_id=' + var).fetchall()
        conn.close()
    elif request.method == 'PUT':
        posts = conn.execute('SELECT * FROM Location WHERE company_id=' + var).fetchall()
    elif request.method == 'DELETE':
        posts = conn.execute('SELECT * FROM Location WHERE company_id=' + var).fetchall()
    return str(posts), 200

@app.route('/api/v1/sensor/', methods=["GET","PUT","DELETE"])
def sensor():
    var  = request.args.get('var', None)
    conn = get_db_connection()
    if request.method == 'GET':
        if var == "all":
            posts = conn.execute('SELECT * FROM Sensor').fetchall()
        else:
            posts = conn.execute('SELECT * FROM Sensor WHERE sensor_api_key=' + var).fetchall()
        conn.close()
    elif request.method == 'PUT':
        posts = conn.execute('SELECT * FROM Sensor WHERE sensor_api_key=' + var).fetchall()
    elif request.method == 'DELETE':
        posts = conn.execute('SELECT * FROM Sensor WHERE sensor_api_key=' + var).fetchall()
    return str(posts), 200

@app.route('/api/v1/sensor_data/', methods=["POST","GET"])
def sensor_data():
    var  = request.args.get('var', None)
    api_key = var['sensor_api_key']
    conn = get_db_connection()
    if request.method == 'POST':
        api_key_server = conn.execute('SELECT * FROM Sensor WHERE sensor_api_key =' + api_key).fetchall()
        if api_key_server == None:
            conn.close()
            return 'Failed: Not matched api_key, try again', 400
        else:
            posts = conn.execute('INSERT INTO Sensor_Data(ID_sensor,Data) VALUES(' + var['data'] + ')').fetchall()
            conn.close()
            return 'created', 201
    elif request.method == 'GET':
        server_company_api_key = conn.execute('SELECT * FROM Sensor WHERE sensor_api_key =' + api_key).fetchall()
        if server_company_api_key == var['company_api_key']:
            return str(posts), 201
        else:
            return 400
    return 'raro',400