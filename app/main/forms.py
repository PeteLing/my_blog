from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

#various Form for view
class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')
