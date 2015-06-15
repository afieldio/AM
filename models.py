from sqlalchemy import Column, Integer, String, Float, DateTime, func
from database import Base
import datetime

class Sensors(Base):
	__tablename__ = 'sensors'
	pk = Column(Integer, primary_key=True)
	sump_temp = Column(Float)
	air_temp = Column(Float)
	# flow_1 = db.Column(db.Float(2))
	# flow_2 = db.Column(db.Float(2))
	# water_htr = db.Column(db.Boolean)
	# air_htr = db.Column(db.Boolean)
	# water_pump = db.Column(db.Boolean)
	# air_pump = db.Column(db.Boolean)
	# fish_temp = db.Column(db.Float(2))
	
	date = Column(DateTime, default=func.now())


	def __init__(self, sump_temp=None, air_temp=None, date=None):
		self.sump_temp = sump_temp
		self.air_temp = air_temp
		self.date = date


	def __repr__(self):
		# return "{'Temp':self.sump_temp, 'Time': self.date}"
		# # return '<Time %r >' % self.date


 		return "{Sensors={'sump_temp':'%s', 'air_temp':'%s', 'date':%s'}" % (
                                self.sump_temp, self.air_temp, self.date)