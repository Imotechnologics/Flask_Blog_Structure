from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField

#Create a Search Form
class SearchForm(FlaskForm):
    searched =StringField("Searched", validators=[DataRequired()])
    submit=SubmitField("Submit")


#createLogin Form:
class LoginForm(FlaskForm):
    username=StringField("Username", validators=[DataRequired()])
    password=PasswordField("Password", validators=[DataRequired()])
    submit=SubmitField("Submit")

#Create a Post Form
class PostForm(FlaskForm):
    title=StringField("Title", validators=[DataRequired()])
    #content=StringField("Content", validators=[DataRequired()], widget=TextArea())
    content = CKEditorField('Content', validators=[DataRequired()])
    author=StringField("Author")
    slug=StringField("Slug", validators=[DataRequired()])
    submit=SubmitField("Submit")

#create Form Class
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    favorite_color=StringField("Favorite Color")
    about_author=TextAreaField("About author")
    password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo('password_hash2', message='Passwords Must Match!')])
    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Submit") 

#Password Form
class PasswordForm(FlaskForm):
    email = StringField("Whats your Email", validators=[DataRequired()])
    password_hash = PasswordField("Whats your Password", validators=[DataRequired()])
    submit = SubmitField("Submit")   

#create Form Class
class NamerForm(FlaskForm):
    name = StringField("Whats your name", validators=[DataRequired()])
    submit = SubmitField("Submit")
