from flask import Flask
from flask import abort
from flask.ext.script import Manager
from flask import render_template
from flask.ext.bootstrap import Bootstrap
import pdb

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

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
		}

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


if __name__ == '__main__':
	app.run(debug=True)
	#manager.run()
