from notesNThings.application.models import db
from sqlalchemy import Table, Column, Integer, ForeignKey, UniqueConstraint

subscriptionTable = Table(
    'subscriptions',
    db.Model.metadata,
    Column('userid', Integer, ForeignKey('users.uid')),
    Column('courseid', Integer, ForeignKey('courses.courseid')),
    UniqueConstraint('userid', 'courseid')
)
