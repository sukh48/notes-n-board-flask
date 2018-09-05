import os
import flask.ext.restless

from sys import path
from flask import Flask
from flask import redirect, request
from flask import render_template

from flask.ext.sqlalchemy import SQLAlchemy
from application.models import db

from application.controllers import users_controller
from application.controllers import notes_controller
from application.controllers import courses_controller
from application.controllers import home_controller
from application.controllers import messages_controller
from application.controllers import comments_controller

import json

app = Flask(__name__)
app.debug = True

# need to find a way to dynamically find the config file's path
print("> configuring from file: %s\n" % app.instance_path+"/config/config.py")
app.config.from_pyfile(app.instance_path+"/config/config.py")

print app.config['SQLALCHEMY_DATABASE_URI']

print("> initializing database\n")
db.init_app(app)

# Extensions like Flask-SQLAlchemy now know what the "current" app
# is while within this block. Therefore, you can now run........

print("> creating database")
with app.app_context():        
	db.create_all()

# Create the Flask-Restless API manager.
restless_manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

messages_controller.create_message_api(restless_manager)
home_controller.create_home_api(restless_manager)
users_controller.create_user_api(restless_manager)
notes_controller.create_note_api(restless_manager)
courses_controller.create_course_api(restless_manager)
comments_controller.create_comment_api(restless_manager)

@app.route('/')
def index():
	return render_template('index.html') 
	# redirect('index.html')

@app.route('/login')
def login():
	return 'login'
