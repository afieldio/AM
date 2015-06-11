from flask.ext.wtf import Form
from wtforms import BooleanField

class SwitchState(Form):
	water = BooleanField('water', default=False)
	air = BooleanField('air', default=False)
	light = BooleanField('light', default=False)
