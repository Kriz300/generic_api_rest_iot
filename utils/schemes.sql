DROP TABLE IF EXISTS admin;
DROP TABLE IF EXISTS company;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS sensor;
DROP TABLE IF EXISTS sensor_data;

CREATE TABLE admin(
    admin_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE company(
    company_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    company_api_key TEXT NOT NULL
);

CREATE TABLE location(
    location_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    company_ID INTEGER NOT NULL,
    location_name TEXT NOT NULL,
    location_country TEXT NOT NULL,
    location_city TEXT NOT NULL,
    location_meta TEXT NOT NULL,
    FOREIGN KEY (company_ID) REFERENCES company (company_ID)
);

CREATE TABLE sensor(
    location_ID INTEGER NOT NULL,
    sensor_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_name TEXT NOT NULL,
    sensor_category TEXT NOT NULL,
    sensor_meta TEXT NOT NULL,
    sensor_api_key TEXT NOT NULL,
    FOREIGN KEY (location_ID) REFERENCES location (location_ID)
);

CREATE TABLE sensor_data(
    sensor_ID INTEGER NOT NULL,
    data TEXT NOT NULL,
    time INTEGER NOT NULL,
    FOREIGN KEY (sensor_ID) REFERENCES sensor (sensor_ID)
);