from flask import Flask
from models import Sensors
from database import db_session

def get_sump_temp():
	st = db_session.query(Sensors).all()


	#.order_by(Sensors.id.desc()).first()
	print st

	#Sensors.query.order_by(Sensors.id.desc()).first()
	return st