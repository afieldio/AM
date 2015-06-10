from flask import Flask, request
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
from flask.ext.migrate import Migrate, MigrateCommand
from forms import SwitchState


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
	st = sensors.get_sump_temp()
	# print st.sump_temp
	#st = '10'
	
	return render_template("index.html", st=st)

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/events')
def events():
	# data = Sensors.query.all()
	d = sensors.__table__.columns
	print d

	return render_template("events.html", data=data)

@app.route('/lightState', methods=["GET", "POST"])
def _lightState():
	form = SwitchState(request.form)

    # if request.form['onoffswitch=on']:
    #     print "Light is On"
    # else:
    #     print "Light is Off"
	print form.water.value
	return ""

@app.route('/events/<id>')
def event_detail(id):
	
	return render_template("events_detail.html", event=event)



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()



if __name__ == '__main__':
	app.run(debug=True)
	#manager.run()
