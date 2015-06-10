from flask.ext.wtf import Form
from wtforms import BooleanField

class SwitchState(Form):
	water = BooleanField('water')
