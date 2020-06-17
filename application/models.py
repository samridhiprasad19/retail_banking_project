import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class User(db.Document):
    customer_ssn_id     =   db.IntField(unique=True )
    password    =   db.StringField( )
    customer_name  =   db.StringField( max_length=50 )
    customer_Address   =   db.StringField( max_length=500 )
    customer_age       =   db.IntField( max_length=5 )
    customer_state  =   db.StringField( max_length=100 )
    customer_city   =   db.StringField( max_length=100 )
   
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)    


class Account(db.Document):
    account_id=db.IntField(unique=True)
    customer_ssn_id = db.IntField()
    account_type = db.StringField()
    deposit_amount= db.IntField()
    transaction_date=db.DateTimeField(default=datetime.datetime.now)
  
