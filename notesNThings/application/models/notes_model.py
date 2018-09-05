from notesNThings.application.models import db
import json
from random import *

class Note (db.Model):
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'notes' 
    uid = db.Column(db.Integer, primary_key = True)
    stored_as = db.Column(db.String(64), unique=True)
    file_name = db.Column(db.String(32))
    owner = db.Column(db.Integer, db.ForeignKey('users.uid'))
    contents = db.Column(db.String(65000))

    def __init__(self, file_name, owner, contents):
        self.file_name = file_name
        self.stored_as = randint(10000000000000000000,100000000000000000000)
        self.owner     = owner
        self.contents  = contents
