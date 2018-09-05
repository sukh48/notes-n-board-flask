from notesNThings.application.models import db
from notesNThings.application.models.comment_model import Comment
import json

class Message (db.Model): 
    # Setting the table name and
    # creating columns for various fields
    __tablename__ = 'messages'
    messageid = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(455))
    message = db.Column(db.Text())
    posttime = db.Column(db.DateTime)
    courseid = db.Column(db.Integer, db.ForeignKey('courses.courseid'))
    userid = db.Column(db.Integer, db.ForeignKey('users.uid'))
    comments = db.relationship('Comment', backref='message',lazy='dynamic')

    def __init__(self, title, message, posttime, courseid, userid):
        self.title = title
        self.message = message
        self.posttime = posttime
        self.courseid = courseid
        self.userid = userid

    def course(self):
        return self.courseid

    def user(self):
        return self.userid

    def comment_ids(self):
        a = Comment.query.filter(Comment.userid == self.userid)
        a = a.filter(Comment.messageid == self.messageid)

        commentids_list = []
        for item in a:
            print item.comment
            commentids_list.append(str(item.commentid))
        return commentids_list