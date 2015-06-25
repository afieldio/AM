from sqlalchemy import Column, Integer, String, Float, DateTime, func, Boolean
from database import Base
import datetime

class Sensors(Base):
	__tablename__ = 'sensors'
	pkS = Column(Integer, primary_key=True)
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
<<<<<<< HEAD
=======
>>>>>>> 57194fbf36854ce277ed1e3f7f04bf4644f1c562


	def __repr__(self):
 		return "{Sensors={'sump_temp':'%s', 'air_temp':'%s', 'date':%s'}" % (
                                self.sump_temp, self.air_temp, self.date)


class Switches(Base):
	__tablename__ = 'switches'
	pkSw = Column(Integer, primary_key=True)
	waterSw = Column(Boolean)
	airSw = Column(Boolean)
	lightSw = Column(Boolean)
	dateSw = Column(DateTime, default=func.now())

	def __init__(self, waterSw=None, airSw=None, lightSw=None, dateSw=None):
		self.waterSw = waterSw
		self.airSw = airSw
		self.lightSw = lightSw

		self.dateSw = dateSw

		# super(Switches, self).__init__()

	def __repr__(self):
 		return "{Switches={'waterSw':'%s', 'airSw':'%s', 'lightSw':'%s','dateSw':%s'}" % (self.waterSw, self.airSw, self.lightSw, self.dateSw)

