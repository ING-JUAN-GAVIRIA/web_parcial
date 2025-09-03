# forms.py — Flask-WTF forms
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField, SelectField
from wtforms.fields import DateField, TimeField
from wtforms.validators import DataRequired, Email, NumberRange, Length

class EventForm(FlaskForm):
    title = StringField("Título", validators=[DataRequired(), Length(max=100)])
    slug = StringField("Slug (url)", validators=[DataRequired(), Length(max=120)])
    description = TextAreaField("Descripción", validators=[DataRequired()])
    date = DateField("Fecha", validators=[DataRequired()], format="%Y-%m-%d")
    time = TimeField("Hora", validators=[DataRequired()], format="%H:%M")
    location = StringField("Ubicación", validators=[DataRequired(), Length(max=120)])
    category = SelectField("Categoría", validators=[DataRequired()], choices=[])
    max_attendees = IntegerField("Cupo máximo", validators=[DataRequired(), NumberRange(min=1, max=10000)])
    featured = BooleanField("Destacado")

class RegisterForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(), Length(max=80)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
