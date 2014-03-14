#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tinkerforge.ip_connection import IPConnection
from os import path, access, R_OK, W_OK
import configparser, time


cfg_filename = 'example.cfg'
local_db = 'weather.db'
PATH = ('./' + cfg_filename)
HOST = "localhost"
PORT = 4223
SleepTime = 0.5
barometer_brick = None
humidity_brick = None
gps_brick = None
illuminance_brick = None

#------------------------- Local DB variables --------------------------- 

date_table = ('''CREATE TABLE IF NOT EXISTS date(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                created_at TIMESTAMP)
                ''')

wd_table = ('''CREATE TABLE IF NOt EXISTS weatherdata(
                uid VARCHAR(5),
                device_name VARCHAR(20),
                value REAL,
                keyword VARCHAR(20),
                date_id INTEGER,
                FOREIGN KEY(date_id) REFERENCES date(id))
                ''')

#---------------------------------- function to create the config file if it doesn`t exist ----------------------------------------

def create_configfile():

    cfg = configparser.RawConfigParser()
    cfg.add_section('Connection')
    cfg.set('Connection', 'Host', HOST)
    cfg.set('Connection', 'Port', PORT)
    cfg.set('Connection', 'SleepTime', SleepTime)

    with open(cfg_filename, 'w') as configfile:
        cfg.write(configfile)
    
    """print ('Config Datei erstellt')"""

#---------------------------------- callback to get information from Bricklet`s ----------------------------------------

def bricklet_callback(uid, connected_uid, position, hardware_version, firmware_version, device_identifier, enumeration_type):
    
    if device_identifier == 221:
        global barometer_brick
        barometer_brick = { "Bricklet_Name" : "Barometer", "Bricklet_UID" : uid, "Bricklet_Position" : position, "Bricklet_Firmware" : firmware_version } 
        #dictionary for barometer brick
    if device_identifier == 222: 
        global gps_brick
        gps_brick = { "Bricklet_Name" : "GPS", "Bricklet_UID" : uid, "Bricklet_Position" : position, "Bricklet_Firmware" : firmware_version}
        #dictionary for GPS brick
    if device_identifier == 27: 
        global humidity_brick
        humidity_brick = { "Bricklet_Name" : "Humidity", "Bricklet_UID" : uid, "Bricklet_Position" : position, "Bricklet_Firmware" : firmware_version }
        #dictionary for humidity brick
    if device_identifier == 21: 
        global illuminance_brick
        illuminance_brick = { "Bricklet_Name" : "Illuminance", "Bricklet_UID" : uid, "Bricklet_Position" : position, "Bricklet_Firmware" : firmware_version }
        #dictionary for illuminance brick
        
#---------------------------------- check if config file exists  ----------------------------------------
def configfile_exists():        
    if path.isfile(PATH) == False:
        create_configfile()
    """else:
        print ('Datei ist bereits vorhanden')"""

#---------------------------------- build connection between masterbrick and bricklets ----------------------------------------
def write_bricklets_into_configfile():    
    #if path.isfile(PATH) and access(PATH, R_OK) and access(PATH, W_OK) == True:  # check if config file exists and is readable and writeable
    #if __name__ == "__main__":
            
        ipcon = IPConnection() 
            
        cfg = configparser.ConfigParser()
            
        cfg.read(cfg_filename) # open config file to read
            
        port = cfg.getint('Connection', 'Port') # get port entry from config file
           
        host = cfg.get('Connection', 'Host') # get host entry from config file
            
        sleeptime = cfg.getfloat('Connection', 'SleepTime')  # get the sleeptime from config file
            
        ipcon.connect(HOST, PORT) 
            
        ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, bricklet_callback)
            
        ipcon.enumerate()
            
        time.sleep(sleeptime)   # sleeptime until all bricklets have answered
            
    #----------------------------------put barometer entrys into config file  ----------------------------------------
                
        if cfg.has_section(barometer_brick["Bricklet_Name"]) == False:
            cfg.add_section(barometer_brick["Bricklet_Name"])
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag Section Barometer erstellt')
            else:
                print ('Eintrag existiert')"""
            
        if cfg.has_option(barometer_brick["Bricklet_Name"], 'Bricklet_UID') == False:    
            cfg.set(barometer_brick["Bricklet_Name"], 'Bricklet_UID', barometer_brick["Bricklet_UID"])
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag UID erstellt')
            else:
                print ('Eintrag existiert')"""
            
        if cfg.has_option(barometer_brick["Bricklet_Name"], 'Bricklet_Position') == False:    
            cfg.set(barometer_brick["Bricklet_Name"], 'Bricklet_Position', barometer_brick["Bricklet_Position"])
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag Position erstellt')
            else:
                print ('Eintrag existiert')"""
            
        if cfg.has_option(barometer_brick["Bricklet_Name"], 'Bricklet_Firmware') == False:    
            cfg.set(barometer_brick["Bricklet_Name"], 'Bricklet_Firmware', str(barometer_brick["Bricklet_Firmware"]))
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag Firmware erstellt')
            else:
                #print ('Eintrag existiert')"""
                
    #----------------------------------put gps entrys into config file ----------------------------------------
            
        if cfg.has_section(gps_brick["Bricklet_Name"]) == False:
            cfg.add_section(gps_brick["Bricklet_Name"])
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag Section Barometer erstellt')
            else:
                print ('Eintrag existiert')"""
            
        if cfg.has_option(gps_brick["Bricklet_Name"], 'Bricklet_UID') == False:    
            cfg.set(gps_brick["Bricklet_Name"], 'Bricklet_UID', gps_brick["Bricklet_UID"])
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag UID erstellt')
            else:
                print ('Eintrag existiert')"""
            
        if cfg.has_option(gps_brick["Bricklet_Name"], 'Bricklet_Position') == False:    
            cfg.set(gps_brick["Bricklet_Name"], 'Bricklet_Position', gps_brick["Bricklet_Position"])
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag Position erstellt')
            else:
                print ('Eintrag existiert')"""
            
        if cfg.has_option(gps_brick["Bricklet_Name"], 'Bricklet_Firmware') == False:    
            cfg.set(gps_brick["Bricklet_Name"], 'Bricklet_Firmware', str(gps_brick["Bricklet_Firmware"]))
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag Firmware erstellt')
            else:
                print ('Eintrag existiert')"""
                
    #----------------------------------put humidity entrys into config file ----------------------------------------
            
        if cfg.has_section(humidity_brick["Bricklet_Name"]) == False:
            cfg.add_section(humidity_brick["Bricklet_Name"])
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag Section Barometer erstellt')
            else:
                print ('Eintrag existiert')"""
            
        if cfg.has_option(humidity_brick["Bricklet_Name"], 'Bricklet_UID') == False:    
            cfg.set(humidity_brick["Bricklet_Name"], 'Bricklet_UID', humidity_brick["Bricklet_UID"])
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag UID erstellt')
            else:
                print ('Eintrag existiert')"""
            
        if cfg.has_option(humidity_brick["Bricklet_Name"], 'Bricklet_Position') == False:    
            cfg.set(humidity_brick["Bricklet_Name"], 'Bricklet_Position', humidity_brick["Bricklet_Position"])
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag Position erstellt')
            else:
                print ('Eintrag existiert')"""
            
        if cfg.has_option(humidity_brick["Bricklet_Name"], 'Bricklet_Firmware') == False:    
            cfg.set(humidity_brick["Bricklet_Name"], 'Bricklet_Firmware', str(humidity_brick["Bricklet_Firmware"]))
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag Firmware erstellt')
            else:
                print ('Eintrag existiert')"""
                
    #----------------------------------put illuminance entrys into config file ----------------------------------------
            
        if cfg.has_section(illuminance_brick["Bricklet_Name"]) == False:
            cfg.add_section(illuminance_brick["Bricklet_Name"])
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag Section Barometer erstellt')
            else:
                print ('Eintrag existiert')"""
            
        if cfg.has_option(illuminance_brick["Bricklet_Name"], 'Bricklet_UID') == False:    
            cfg.set(illuminance_brick["Bricklet_Name"], 'Bricklet_UID', illuminance_brick["Bricklet_UID"])
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag UID erstellt')
            else:
                print ('Eintrag existiert')"""
            
        if cfg.has_option(illuminance_brick["Bricklet_Name"], 'Bricklet_Position') == False:    
            cfg.set(illuminance_brick["Bricklet_Name"], 'Bricklet_Position', illuminance_brick["Bricklet_Position"])
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag Position erstellt')
            else:
                print ('Eintrag existiert')"""
            
        if cfg.has_option(illuminance_brick["Bricklet_Name"], 'Bricklet_Firmware') == False:    
            cfg.set(illuminance_brick["Bricklet_Name"], 'Bricklet_Firmware', str(illuminance_brick["Bricklet_Firmware"]))
            with open(cfg_filename, 'w') as configfile:
                cfg.write(configfile)
                """print ('Eintrag Firmware erstellt')
            else:
                print ('Eintrag existiert')"""
            
        ipcon.disconnect()   # disconnect connection between masterbrick and bricklet

