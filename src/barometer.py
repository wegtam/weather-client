#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tinkerforge.ip_connection import IPConnection,Error 
from tinkerforge.bricklet_barometer import Barometer
from create_cfg import local_db, cfg_filename, wd_table, date_table  # include variables from create_cfg
from os import path, access, R_OK, W_OK
from datetime import date, datetime
import configparser, sqlite3

def get_airpressure():

    ipcon = IPConnection() # Create IP connection

    cfg = configparser.ConfigParser()

    cfg.read(cfg_filename) # open config file to read from

    port = cfg.getint('Connection', 'Port') # get port entry from config file

    host = cfg.get('Connection', 'Host') # get host entry from config file

    uid = cfg.get('Barometer', 'bricklet_uid') # uid port entry from config file

    try:
        ipcon.connect(host, port) # Connect to brickd

        b = Barometer(uid, ipcon) # Create device object

        air_pressure = b.get_air_pressure()/1000.0 # Get current air pressure (unit is mbar/1000)

        altitude = b.get_altitude()/100.0
    except Error:
        
        print("Fehlermeldung: Keine Verbindung zum Barometer-Bricklet möglich")
    else:

        db = sqlite3.connect(local_db) # build connection to local database

        c = db.cursor() # create cursor

        c.execute(date_table) # create date table 

        c.execute(wd_table) # create weatherdata table

        now = datetime.now() # create a date object

        c.execute('''INSERT INTO date(created_at) VALUES(?)''', (now,)) # insert the actually date and time into the date table

        id = c.lastrowid # get recent id entry from database

        c.execute('''INSERT INTO weatherdata(uid , value, keyword, date_id, device_name) VALUES(?,?,?,?,?)''', (uid,air_pressure,'air_pressure',id,'barometer',))
    # insert the uid, device name the id from the date table an die humdity value into the weather table

        c.execute('''INSERT INTO weatherdata(uid , value, keyword, date_id, device_name) VALUES(?,?,?,?,?)''', (uid,altitude,'altitude',id,'barometer',))

        db.commit() # save creates and inserts permanent  

        print('Air Pressure: ' + str(air_pressure) + ' mbar')
        print()
        print('Altitude: ' + str(altitude) + ' m')
        ipcon.disconnect()


