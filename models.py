from sqlalchemy import Column, Integer, String, Float, DateTime, func, Boolean
from database import Base
import datetime

class Sensors(Base):
	__tablename__ = 'sensors'
	pkS = Column(Integer, primary_key=True)
	sump_temp = Column(Float)
	air_temp = Column(Float)
	light_lux = Column(Float)
	fish_temp = Column(Float)
	grow_temp = Column(Float)
	date = Column(DateTime, default=func.now())


	# def __init__(self, sump_temp=None, air_temp=None, date=None):
	# 	self.sump_temp = sump_temp
	# 	self.air_temp = air_temp
	# 	self.date = date


	def __repr__(self):
 		return "{Sensors={'sump_temp':'%s', 'air_temp':'%s', 'light_lux:%s', 'fish_temp':'%s', 'grow_temp':'%s', 'date':%s'}" % (self.sump_temp, self.air_temp, self.light_lux, self.fish_temp, self.grow_temp, self.date)


class Switches(Base):
	__tablename__ = 'switches'
	pkSw = Column(Integer, primary_key=True)
	waterSw = Column(Boolean)
	airSw = Column(Boolean)
	lightSw = Column(Boolean)
	dateSw = Column(DateTime, default=func.now())

	# def __init__(self, waterSw=None, airSw=None, lightSw=None, dateSw=None):
	# 	self.waterSw = waterSw
	# 	self.airSw = airSw
	# 	self.lightSw = lightSw

	# 	self.dateSw = dateSw

		# super(Switches, self).__init__()

	def __repr__(self):
 		return "{Switches={'waterSw':'%s', 'airSw':'%s', 'lightSw':'%s','dateSw':%s'}" % (self.waterSw, self.airSw, self.lightSw, self.dateSw)

