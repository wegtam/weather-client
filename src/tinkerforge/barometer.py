#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223

UID_Barometer = None 
UID_Humidity = None
UID_AmbientLight = None
UID_GPS = None
Pos_Humidity = None
		

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_barometer import Barometer
import time

def my_testcallback(uid, connected_uid, position, hardware_version, firmware_version,
                 device_identifier, enumeration_type):
	
	if device_identifier == 221: 
		global UID_Barometer
		UID_Barometer = uid
		return UID_Barometer
	if device_identifier == 222: 
		global UID_GPS
		UID_GPS = uid
		return UID_GPS
	if device_identifier == 27: 
		global UID_Humidity
		UID_Humidity = uid
		return UID_Humidity
	if device_identifier == 21: 
		global UID_AmbientLight
		UID_AmbientLight = uid
		return UID_AmbientLight
		

		
if __name__ == "__main__":
	 
	ipcon = IPConnection() 
	
	ipcon.connect(HOST, PORT) 
	
	ipcon.register_callback(IPConnection.CALLBACK_ENUMERATE, my_testcallback)
	
	ipcon.enumerate()
	
	while UID_Barometer == None or (UID_Humidity == None) or (UID_AmbientLight == None):
		time.sleep(0.000001)
	else:
		print('')
		print('UID_Barometer: ' + str(UID_Barometer))
		print('UID_GPS: ' + str(UID_GPS))
		print('UID_Humidity: ' + str(UID_Humidity))
		print('UID_AmbientLight: ' + str(UID_AmbientLight))
		print('')
	
	
	#b = Barometer(UID_Barometer, ipcon) # die uid`s brauch ich um die bricklets anzusprechen
	
	#air_pressure = b.get_air_pressure()/1000.0

	#print('Air Pressure: ' + str(air_pressure) + ' mbar')

	#altitude = b.get_altitude()/100.0

	#print('Altitude: ' + str(altitude) + ' m')
	
	#print('')
	#input('Press any key to exit\n')
	
	ipcon.disconnect()
