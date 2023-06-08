from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import base64
import os

def b64encode(value):
    encoded_bytes = base64.b64encode(value.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///../blogdatabase.db'
app.config['SECRET_KEY']='644003d590ba593d0e98a7b7caed801e'

# Set the path to the static folder
# app.static_folder = 'static'

# Set the path to the upload folder
# app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'images')

# Ensure the upload folder exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"
login_manager.login_message="Please login first!"

# app.jinja_env.filters['lc_name'] = locale_code_to_name_filte
app.jinja_env.filters['b64encode'] = b64encode
from blog import routes