from flask_wtf import FlaskForm
from wtforms.fields import PasswordField,TextAreaField,StringField,SubmitField
from wtforms.validators import DataRequired,Email,Length,EqualTo

class UploadForm(FlaskForm):
    description=TextAreaField(label='The Descriptiom of Software: ',validators=[DataRequired(message='Descrption needed'),Length(min=20,max=150,message='length of description shall range in 20 to 50 characters')])\
    #software = FileField(validators=[FileRequired()])
    username=StringField(label='User Name',validators=[Email(message='enter a valid email'),Length(max=20)])
    password=PasswordField(label='Password',validators=[DataRequired(message='Please Type in the Password'),Length(min=5,message='minimum of 5 characters')])
    submit=SubmitField(label='authenticate and upload')

class RegisterForm(FlaskForm):
    roll=StringField(label='Admission Number',validators=[DataRequired(message='enter roll number'),Length(min=10,max=10,message='enter roll number properly')])
    username = StringField(label='User Name', validators=[Email(message='enter a valid email'), Length(max=20)])
    password = PasswordField(label='Password', validators=[DataRequired(message='Please Type in the Password'),
                                                           Length(min=5, message='minimum of 5 characters')])
    password2 = PasswordField(label='Password2', validators=[EqualTo('password',message='passwords must match'),
                                                           Length(min=5, message='minimum of 5 characters')])
    submit = SubmitField(label='REQUEST ID')


class SearchForm(FlaskForm):
    search=StringField('query',validators=[DataRequired()])
    submit=SubmitField('Search')
