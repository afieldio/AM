from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base

class Sensors(Base):
	__tablename__ = 'sensors'
	id = Column(Integer, primary_key=True)
	sump_temp = Column(Float(2))
	# fish_temp = db.Column(db.Float(2))
	# air_temp = db.Column(db.Float(2))
	# flow_1 = db.Column(db.Float(2))
	# flow_2 = db.Column(db.Float(2))
	# water_htr = db.Column(db.Boolean)
	# air_htr = db.Column(db.Boolean)
	# water_pump = db.Column(db.Boolean)
	# air_pump = db.Column(db.Boolean)
	
	date = Column(DateTime)

	def __init__(self, sump_temp=None, date=None):
		self.sump_temp = sump_temp
		self.date = date


	def __repr__(self):
		return '<Sensor %r >' % self.sump_temp
		return '<Time %r >' % self.date