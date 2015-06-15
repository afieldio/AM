from flask import Flask
from models import Sensors
from database import db_session
from sqlalchemy import desc


def get_sump_temp():
	st = Sensors.query.order_by(desc(Sensors.date)).first()
	#import ipdb; ipdb.set_trace()
	return st