import database
import models
import sensors

def sensors_data_grab():
	st = sensors.get_sump_temp();

	sensor_data = Sensors(st, '99.99')
	db_session.add(sensor_data)
	db_session.commit()

def