from flask_wtf import FlaskForm
from wtforms import StringField, IntegerRangeField, SubmitField, SearchField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets import HiddenInput

# your forms go here