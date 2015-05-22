from flask import Flask
from flask import abort
from flask.ext.script import Manager
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
import pdb
import os
import pprint
import sensors
import gviz_api
import json

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
db =SQLAlchemy(app)

@app.route('/')
def index():
	sump_temp = sensors.get_temp()

	return render_template("index.html", sump_temp=sump_temp)

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/events')
def events():
	data=events
	return render_template("events.html", data=data)

@app.route('/events/<id>')
def event_detail(id):
	
	return render_template("events_detail.html", event=event)


def get_temp():
	sump_temp = 10.0
	return sump_temp


class Sensors(db.Model):
	__tablename__ = 'sensors'
	id = db.Column(db.Integer, primary_key=True)
	sump_temp = db.Column(db.Float(2))
	# fish_temp = db.Column(db.Float(2))
	# air_temp = db.Column(db.Float(2))
	# flow_1 = db.Column(db.Float(2))
	# flow_2 = db.Column(db.Float(2))
	# water_htr = db.Column(db.Boolean)
	# air_htr = db.Column(db.Boolean)
	# water_pump = db.Column(db.Boolean)
	# air_pump = db.Column(db.Boolean)
	
	date = db.Column(db.DateTime)

	def __repr__(self):
		return '<Senor %r >' % self.name




if __name__ == '__main__':
	app.run(debug=True)
	#manager.run()
