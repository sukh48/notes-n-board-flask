from notesNThings.application.models import db
from notesNThings.application.models.subscriptions_model import subscriptionTable
from sqlalchemy.orm import relationship, backref

import json

class Course (db.Model): 
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'courses'
    courseid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(9))
    alt_name = db.Column(db.String(255))
    professor = db.Column(db.Integer, db.ForeignKey('users.uid'))

    def __init__(self, name, alt_name, professor):
        self.name = name
        self.alt_name = alt_name
        self.professor = professor
        self.user_ids = []

    def user_ids(self):
        user_id_list = []

        for user in self.users:
            user_id_list.append( str(user.uid) )

        return user_id_list

