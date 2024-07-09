from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileField

class AddProductClass(FlaskForm):
    text = StringField("Product Name", validators=[DataRequired()]) 
    price = IntegerField("Product Price", validators=[DataRequired()])
    description = StringField("Product Description")
    category_id = IntegerField("Category ID")

    #category = SelectField("Category", choices=[("Face", "Face"), ("Body", "Body"), ("Need", "Need")], 
                           #validators=[DataRequired()])
    
    image = FileField("Upload Image")
    image_url = StringField("Image URL")

    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=25)])
    email= StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Passwords should match")])

    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=25)]) 
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])   

    submit = SubmitField("Log In")


