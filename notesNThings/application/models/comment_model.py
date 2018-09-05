from notesNThings.application.models import db
import json

class Comment (db.Model): 
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'comments'
    commentid = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text())
    posttime = db.Column(db.DateTime)
    userid = db.Column(db.Integer, db.ForeignKey('users.uid'))
    messageid = db.Column(db.Integer, db.ForeignKey('messages.messageid'))

    def __init__(self, comment, posttime, userid, messageid):
        self.comment = comment
        self.posttime = posttime
        self.messageid = messageid
        self.userid = userid