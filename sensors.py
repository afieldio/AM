from flask import Flask
from models import Sensors
from database import db_session
from sqlalchemy import desc
#from w1thermsensor import W1ThermSensor

def get_sump_temp():
	
	#sensor = W1ThermSensor()
	#sump_temp = sensor.get_temperature()
	# print sump_temp
	sump_temp = 99.99
	air_temp = 99.99
	st = Sensors(sump_temp=sump_temp, air_temp='99.99')
	db_session.add(st)
	db_session.commit()

	#import ipdb; ipdb.set_trace()
	return st

if __name__ == '__main__':
	get_sump_temp()