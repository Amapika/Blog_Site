from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                                     validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
                                validators=[DataRequired(), Email() ])

    password = PasswordField('Password',
                                        validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password',
                                                        validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Signup') 

    def validate_username(self,username):
        
        user = User.query.filter_by(username=username.data).first() 
        
        if user:
            raise ValidationError('That username is already taken.Please Choose some different username')
    
    def validate_email(self,email):
        
        user = User.query.filter_by(email=email.data).first() 
        
        if user:
            raise ValidationError('That email_id is already taken.Please Choose some different email_id')


class LoginForm(FlaskForm):
   
    email = StringField('Email',
                                validators=[DataRequired(), Email() ])

    password = PasswordField('Password',
                                        validators=[DataRequired()])
    
    remember = BooleanField('Remeber me')

    submit = SubmitField('Login') 
                                                               