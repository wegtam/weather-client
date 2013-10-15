#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_ambient_light import AmbientLight
from create_cfg import local_db, cfg_filename, wd_table, date_table  # include variables from create_cfg
from os import path, access, R_OK, W_OK
from datetime import date, datetime
import configparser, sqlite3

def get_illuminance():
        
    ipcon = IPConnection() # Create IP connection
        
    cfg = configparser.ConfigParser()
            
    cfg.read(cfg_filename) # open config file to read from
            
    port = cfg.getint('Connection', 'Port') # get port entry from config file
            
    host = cfg.get('Connection', 'Host') # get host entry from config file
        
    uid = cfg.get('Illuminance', 'bricklet_uid') # get uid entry from config file

    ipcon.connect(host, port) # Connect to brickd
    
    al = AmbientLight(uid, ipcon) # Create device object
    
    illuminance = al.get_illuminance()/10.0 # Get current humidity (unit is %RH/10)
        
    db = sqlite3.connect(local_db) # build connection to local database
    
    c = db.cursor() # create cursor
    
    c.execute(date_table) # create date table 
    
    c.execute(wd_table) # create weatherdata table
    
    now = datetime.now() # create a date object
    
    c.execute('''INSERT INTO date(created_at) VALUES(?)''', (now,)) # insert the actually date and time into the date table
    
    id = c.lastrowid # get recent id entry from database 
    
    c.execute('''INSERT INTO weatherdata(uid ,value, keyword, date_id, device_name) VALUES(?,?,?,?,?)''', (uid,illuminance,'illuminance', id,'illuminance',))
    # insert the uid, device name the id from the date table an die lightness value into the weather table
    
    db.commit() # save creates and inserts permanent
        
    print('Illuminance: ' + str(illuminance) + ' Lux')
    print()
    
    ipcon.disconnect()

