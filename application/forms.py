from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User

class LoginForm(FlaskForm):
    email   = StringField("Customer_SSN_ID", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
	customer_ssn_id = StringField("Customer SSN ID",validators=[DataRequired()]) 
	password = PasswordField("Password",validators=[DataRequired()])
	customer_name = StringField("Customer Name",validators=[DataRequired()])
	customer_Address = StringField("Address",validators=[DataRequired()])
	customer_age = StringField("Age",validators=[DataRequired()])
	customer_state = StringField("State",validators=[DataRequired()])
	customer_city = StringField("City",validators=[DataRequired()])
	submit = SubmitField("Submit")
class CustomerSearch(FlaskForm):
	ssn_id = StringField("Enter SSN ID") 
	customer_id = StringField("Enter Customer ID")
	view = SubmitField("View")
class AccountSearch(FlaskForm):
	account_id = StringField("Enter Account ID") 
	customer_id = StringField("Enter Customer ID")
	View = SubmitField("View")



    