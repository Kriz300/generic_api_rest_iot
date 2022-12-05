cursor.execute("CREATE TABLE Admin(Username TEXT NOT NULL, Password TEXT NOT NULL)")
cursor.execute("CREATE TABLE Company(ID INTEGER NOT NULL, Company_name TEXT NOT NULL, Company_api_key TEXT NOT NULL UNIQUE)")
cursor.execute("CREATE TABLE Location(Company_id INTEGER NOT NULL, Location_name TEXT NOT NULL, Location_country TEXT NOT NULL, Location_city TEXT NOT NULL, Location_meta TEXT NOT NULL)")
cursor.execute("CREATE TABLE Sensor(Location_id INTEGER NOT NULL, Sensor_id INTEGER NOT NULL, Sensor_name TEXT NOT NULL, Sensor_category TEXT NOT NULL, Sensor_meta TEXT NOT NULL, Sensor_api_key TEXT NOT NULL UNIQUE)")
cursor.execute("CREATE TABLE Sensor_Data(ID_sensor TEXT NOT NULL, Data TEXT NOT NULL)")