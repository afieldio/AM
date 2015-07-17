from flask import Flask
from models import Sensors
from database import db_session
from sqlalchemy import desc
from w1thermsensor import W1ThermSensor
import Adafruit_BMP.BMP085 as BMP085

def get_sensor_data():
	
	sensor = W1ThermSensor()
	sump_temp = sensor.get_temperature()
	print sump_temp
	# sump_temp = 99.99
	# air_temp = 99.99
	air_Sensor = BMP085.BMP085()
	air_temp = air_Sensor.read_temperature()


	st = Sensors(sump_temp=sump_temp, air_temp=air_temp)
	db_session.add(st)
	db_session.commit()

	#import ipdb; ipdb.set_trace()
	return st

if __name__ == '__main__':
	get_sensor_data()
