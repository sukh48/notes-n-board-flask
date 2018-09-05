from notesNThings.application.models import db
from notesNThings.application.models.subscriptions_model import subscriptionTable
from notesNThings.application.models.courses_model import Course
from sqlalchemy.orm import relationship, backref

import json

ROLE_USER = 0
ROLE_ADMIN = 1

class User (db.Model): 
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), unique=True)
    email    = db.Column(db.String(64), unique=True)
    password = db.Column(db.String())
    admin    = db.Column(db.Boolean)
    courses = relationship("Course", secondary = subscriptionTable, backref="users")

    def __init__(self, username, password, email, admin):
        self.username = username
        self.password = password
        self.email = email
        self.admin = admin

    def course_ids(self):
        course_id_list = []

        for course in self.courses:
            course_id_list.append( str(course.courseid) )

        return course_id_list
