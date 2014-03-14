#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_barometer import Barometer
from create_cfg import local_db, cfg_filename, wd_table, date_table  # include variables from create_cfg
from os import path, access, R_OK, W_OK
from datetime import date, datetime
import configparser, sqlite3

def get_airpressure(id):
    
    cfg = configparser.ConfigParser()
    
    cfg.read(cfg_filename) # open config file to read from
    
    if cfg.has_section("Barometer") == True:
    
        port = cfg.getint('Connection', 'Port') # get port entry from config file
        
        host = cfg.get('Connection', 'Host') # get host entry from config file
        
        uid = cfg.get('Barometer', 'bricklet_uid') # uid port entry from config file
        
        ipcon = IPConnection() # Create IP connection
        
        ipcon.connect(host, port) # Connect to brickd
        
        b = Barometer(uid, ipcon) # Create device object
        
        air_pressure = b.get_air_pressure()/1000.0 # Get current air pressure (unit is mbar/1000)
        
        altitude = b.get_altitude()/100.0
        
        db = sqlite3.connect(local_db) # build connection to local database
        
        c = db.cursor() # create cursor
        
        c.execute(wd_table) # create weatherdata table
        
        c.execute('''INSERT INTO weatherdata(uid , value, keyword, date_id, device_name) VALUES(?,?,?,?,?)''', (uid,air_pressure,'air_pressure',id,'barometer',))
        # insert the uid, device name the id from the date table an die humdity value into the weather table
        
        c.execute('''INSERT INTO weatherdata(uid , value, keyword, date_id, device_name) VALUES(?,?,?,?,?)''', (uid,altitude,'altitude',id,'barometer',))
        
        db.commit() # save creates and inserts permanent  

        print('Air Pressure: ' + str(air_pressure) + ' mbar')
        print()
        print('Altitude: ' + str(altitude) + ' m')

        ipcon.disconnect()