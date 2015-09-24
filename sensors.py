from flask import Flask
from models import Sensors
from database import db_session
from sqlalchemy import desc
from w1thermsensor import W1ThermSensor
import Adafruit_BMP.BMP085 as BMP085
import tsl2561 as TSL
from oneWire import get_dallas_temps

def get_sensor_data():
	#if settings is local run this else run sensors.

	dallasTemps = get_dallas_temps()
	#import ipdb; ipdb.set_trace()
	print dallasTemps


	sump_temp = dallasTemps['sump_tank']
	fish_temp = dallasTemps['fish_tank']
	grow_temp = dallasTemps['grow_bed']
	#print sump_temp
	# sump_temp = 99.99
	# air_temp = 99.99
	air_Sensor = BMP085.BMP085()
	air_temp = air_Sensor.read_temperature()
	#print air_temp
	light_sensor = TSL.TSL2561()
	light_lux = light_sensor.readLux()
	#light_lux = 100
	#print light_lux


	st = Sensors(sump_temp=sump_temp, air_temp=air_temp, light_lux=light_lux, fish_temp=fish_temp, grow_temp=grow_temp)
	db_session.add(st)
	db_session.commit()

	#import ipdb; ipdb.set_trace()
	return st

if __name__ == '__main__':
	get_sensor_data()
