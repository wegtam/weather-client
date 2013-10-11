#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path, access, R_OK, W_OK
from create_cfg import configfile_exists, write_bricklets_into_configfile # import function from create_cfg.py
from humidity import get_humidity   # import function from humidity.py
from illuminance import get_illuminance # import function from illuminance.py
from barometer import get_airpressure # import function from barometer.py


filename = 'example.cfg'
PATH = ('./' + filename)

if path.isfile(PATH) == False:  # check if config file exists and is readable and writeable

    configfile_exists()

if path.isfile(PATH) and access(PATH, R_OK) and access(PATH, W_OK) == True:

    write_bricklets_into_configfile()

else:
    print("Die Datei " + filename + " existiert nicht oder ist nicht beschreibar")
    
if path.isfile(PATH) and access(PATH, R_OK) and access(PATH, W_OK) == True:
    
    get_humidity()
    
    get_illuminance()
    
    get_airpressure()