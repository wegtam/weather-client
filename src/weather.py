#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path, access, R_OK, W_OK
import urllib3
import configparser, sqlite3
from datetime import date, datetime
from create_cfg import local_db, cfg_filename, date_table, PATH
from create_cfg import configfile_exists, write_bricklets_into_configfile # import function from create_cfg.py
from humidity import get_humidity   # import function from humidity.py
from illuminance import get_illuminance # import function from illuminance.py
from barometer import get_airpressure # import function from barometer.py
from tinkerforge.ip_connection import IPConnection


if path.isfile(PATH) == False:  # check if config file exists

    configfile_exists()

if path.isfile(PATH) and access(PATH, R_OK) and access(PATH, W_OK) == True:

    write_bricklets_into_configfile()

else:
    print("Die Datei " + filename + " existiert nicht oder ist nicht beschreibar")
    
if path.isfile(PATH) and access(PATH, R_OK) and access(PATH, W_OK) == True:
    
    db = sqlite3.connect(local_db) # build connection to local database
    
    c = db.cursor() # create cursor
    
    c.execute(date_table) # create date table

    now = datetime.now() # create a date object
    
    c.execute('''INSERT INTO date(created_at) VALUES(?)''', (now,)) # insert the actually date and time into the date table
    
    db.commit()
    
    id = c.lastrowid # get recent id entry from database
    
    humidity = str(get_humidity(id))
    
    get_illuminance(id)
    
    get_airpressure(id)
    
    http = urllib3.PoolManager()
    #url = 'http://127.0.0.1:8000/save_wd/20/20/20/20/20/1/2'
    url = 'http://127.0.0.1:8000/save_wd/'

    fields = {"humidity": humidity, "temperature": "20", "altitude": "20", "lightness": "20", "air_pressure": "20", "weatherstation_id": "1", "user_id": "2"}
    
    print(fields)
    #r = http.request_encode_url('GET', url)
    r = http.request_encode_body('POST', url, fields=fields)
