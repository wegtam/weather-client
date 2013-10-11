#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path, access, R_OK, W_OK
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_barometer import Barometer
from datetime import date, datetime
import configparser, sqlite3


cfg_filename = 'example.cfg'
db_filename = 'weather.db'

date_table = ('''CREATE TABLE IF NOT EXISTS date(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                created_at TIMESTAMP)
                ''')

wd_table = ('''CREATE TABLE IF NOt EXISTS weatherdata(
                uid VARCHAR(5),
                device_name VARCHAR(20),
                illuminance REAL,
                rel_humidity REAL,
                air_pressure REAL,
                altitude REAL,
                date_id INTEGER,
                FOREIGN KEY(date_id) REFERENCES date(id))
                ''')

def get_airpressure():
    
    ipcon = IPConnection() # Create IP connection
    
    cfg = configparser.ConfigParser()
    
    cfg.read(cfg_filename) # open config file to read from
    
    port = cfg.getint('Connection', 'Port') # get port entry from config file
    
    host = cfg.get('Connection', 'Host') # get host entry from config file
    
    uid = cfg.get('Barometer', 'bricklet_uid') # uid port entry from config file
    
    ipcon.connect(host, port) # Connect to brickd
    
    b = Barometer(uid, ipcon) # Create device object
    
    air_pressure = b.get_air_pressure()/1000.0 # Get current air pressure (unit is mbar/1000)
    
    altitude = b.get_altitude()/100.0
    
    db = sqlite3.connect(db_filename) # build connection to local database
    
    c = db.cursor() # create cursor
    
    c.execute(date_table) # create date table 
    
    c.execute(wd_table) # create weatherdata table
    
    now = datetime.now() # create a date object
    
    c.execute('''INSERT INTO date(created_at) VALUES(?)''', (now,)) # insert the actually date and time into the date table
    
    id = c.lastrowid # get recent id entry from database
    
    c.execute('''INSERT INTO weatherdata(uid ,air_pressure, altitude, date_id, device_name) VALUES(?,?,?,?,?)''', (uid,air_pressure,altitude,id,'barometer',))
    # insert the uid, device name the id from the date table an die humdity value into the weather table
    
    db.commit() # save creates and inserts permanent  

    print('Air Pressure: ' + str(air_pressure) + ' mbar')
    print()
    print('Altitude: ' + str(altitude) + ' m')

    ipcon.disconnect()