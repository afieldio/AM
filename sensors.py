from flask import Flask
from models import Sensors

def get_sump_temp():
	st = Sensors.query.order_by(Sensors.id.desc()).first()
	return st