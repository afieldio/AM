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
from database import db_session
from models import Sensors



app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
# db =SQLAlchemy(app)

@app.route('/')
def index():
	sump_temp = sensors.get_temp()

	return render_template("index.html", sump_temp=sump_temp)

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/events')
def events():
	data = Sensors.query.all()
	print data

	return render_template("events.html", data=data)

@app.route('/events/<id>')
def event_detail(id):
	
	return render_template("events_detail.html", event=event)


def get_temp():
	sump_temp = 10.0
	return sump_temp



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()



if __name__ == '__main__':
	app.run(debug=True)
	#manager.run()
