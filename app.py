from flask import Flask, request, flash
from flask import abort
from flask.ext.script import Manager
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import pdb
import os
import pprint
import sensors
import gviz_api
import json
from database import db_session
from models import Sensors, Switches
from flask.ext.migrate import Migrate, MigrateCommand
from forms import SwitchState
import pin_control
import Adafruit_BMP.BMP085 as BMP085

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config.from_object('config')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
db =SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
# Main pages


@app.route('/')
def index():
	switchObj = db_session.query(Switches).order_by(Switches.dateSw.desc()).first()
	# import ipdb; ipdb.set_trace()
	st = sensors.get_sensor_data()
	# import ipdb; ipdb.set_trace()
	dateformat = st.date.strftime('%a %d %b  - %H:%M')
	print dateformat
	#st = '10'
	
	bmp = BMP085.BMP085()
	air_temp = bmp.read_temperature()
	#air_temp = 10
	#import ipdb; ipdb.set_trace()

	print air_temp
	return render_template("index.html", st=st, air_temp=air_temp, dateformat=dateformat, switchObj=switchObj)

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/graphs')
def graphs():
	data = db_session.query(Sensors).order_by(Sensors.date.asc()).all()
	# import ipdb; ipdb.set_trace()
	return render_template("graphs.html", data=data)

@app.route('/presentation')
def presentation():
	return render_template("presentation.html")

@app.route('/switchState', methods=["GET", "POST"])
def _switchState():
	
	form = SwitchState(request.form)
	print form.data
	
	water = form.water.data
	light = form.light.data
	air = form.air.data

	print water
	print light
	print air

	sw = Switches(waterSw=water, airSw=air, lightSw=light)
	# import ipdb; ipdb.set_trace()
	db_session.add(sw)

	db_session.commit()


	if form.water.data:
	 	pin_control.turn_on(17)
	else:
	 	pin_control.turn_off(17)

	# if not form.light.data:
	# 	print "Light Off"
	# else:
	# 	print "Light On"

	# if not form.air.data:
	# 	print "Air Off"
	# else:
	# 	print "Air On"


	# import ipdb; ipdb.set_trace()
	return ""

@app.route('/events/<id>')
def event_detail(id):
	
	return render_template("events_detail.html", event=event)



@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()



if __name__ == '__main__':
	app.run('192.168.1.73', debug=True)
	#manager.run()
