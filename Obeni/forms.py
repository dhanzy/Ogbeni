from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField, SubmitField, IntegerField, StringField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo, Required




class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(message='Incorrect Email Address!'), Required(), Length(min=5, max=32)])
    password = PasswordField('Password', validators=[Required(), Length(min=8, max=34)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ShippingForm(FlaskForm):
    firstname = TextField('First Name', validators=[DataRequired(), Length(min=3, max=20)])
    lastname = TextField('Last Name', validators=[Length(min=3, max=20)])
    email = TextField('Email', validators=[Email(message='This Field Requires a Valid Email Address'), DataRequired('Please Enter Your Email Address')])
    address = TextField('Address', validators=[DataRequired()])
    country = SelectField('Country', choices=['Nigeria','Ghana','Togo'])
    state = SelectField('State', choices=['Abia','Adamawa','Akwa-Ibom','Anambra','Bauchi','Bayelsa','Borno','Cross River', 'Delta','Ebonyi','Edo','Ekiti','Enugu','Gombe','Jigawa','Kaduna'], validators=[DataRequired()], default='Ekiti')
    city= TextField('City', validators=[DataRequired()])
    zipcode = TextField('Zip Code', validators=[DataRequired('Zipcode Required')])
    phone =  IntegerField('Phone Number', validators=[DataRequired(message='Please Include Your Phone Number')])