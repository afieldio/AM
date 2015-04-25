from flask import Flask
from flask import abort
from flask.ext.script import Manager
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
import pdb
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
db =SQLAlchemy(app)

Events = [
	{
		'id': '1',
		'image': ' http://lorempixel.com/400/200/sports/',
		'name': 'Event 1',
		'date': '1429709298',
		'description': 'This is a super cool app',
		'location': 'xxx',
	},
	{
		'id': '2',
		'image': ' http://lorempixel.com/400/200/technics/',
		'name': 'Event 2',
		'date': '1429709298',
		'description': 'This is a super cool app again',
		'location': 'xxx',
	},
	{
		'id': '3',
		'image': ' http://lorempixel.com/400/200/fashion/',
		'name': 'Event 3',
		'date': '1429709298',
		'description': 'This is a super cool app again again',
		'location': 'xxx',
	},
]


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/events')
def events():
	data=Events
	return render_template("events.html", data=data)

@app.route('/events/<id>')
def event_id(id):
	index = int(id) - 1
	event = Events[index]
	return render_template("events_detail.html", event=event)

class Events(db.Model):
	__tablename__ = 'events'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	description = db.Column(db.Text)
	date = db.Column(db.DateTime)

	def __repr__(self):
		return '<Event %r >' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username  = db.Column(db.String(64), unique=True, index=True)

	def __repr__(self):
		return '<User %r >' % self.username
		


if __name__ == '__main__':
	app.run(debug=True)
	#manager.run()
