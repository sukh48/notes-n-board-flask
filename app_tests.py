import unittest
import os
import tempfile
import sqlalchemy
import flask
import json
from notesNThings import app, db
from datetime import datetime

from notesNThings.application.models.users_model import User
from notesNThings.application.models.courses_model import Course
from notesNThings.application.models.notes_model import Note
from notesNThings.application.models.message_model import Message
from notesNThings.application.models.comment_model import Comment

TEST_DB = 'postgresql://postgres:password@localhost/notes_n_things_testdb'

class NotesTestCase(unittest.TestCase):
		def setUp(self):
				basedir = os.path.abspath(os.path.dirname(__file__))
				app.config['TESTING'] = True
				app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB
				self.app = app.test_client()
				with app.app_context():
						db.create_all()

		def tearDown(self):
				with app.app_context():
						db.session.remove()
						engine = sqlalchemy.create_engine(TEST_DB)
						metadata = sqlalchemy.MetaData(engine)
						metadata.reflect()
						metadata.drop_all()

		def testCoursesModel(self):
			with app.app_context():
				professor = User(username="Bob", password="dinosaur", email="email@email.com",
					admin = True)
				db.session.add(professor)
				db.session.flush()

				newCourse = Course(name='COMP 1010', alt_name='Computer science', professor=1)
				db.session.add(newCourse)
				db.session.flush()
				self.assertEqual(db.session.query(Course).get(1).name, 'COMP 1010')

				db.session.delete(newCourse)
				db.session.flush()

				self.assertEqual(db.session.query(Course).get(1), None)

		def testUsersModel(self):
			with app.app_context():
				newUser = User(username="Bob", password="dinosaur", email="email@email.com",admin = False)
				db.session.add(newUser)
				db.session.flush()
				self.assertEqual(db.session.query(User).get(1).username, 'Bob')

				with app.test_client() as c:
					resp = c.get('api/users/1')
					data = json.loads(resp.data)
					self.assertEqual(data['user']['username'], "Bob")
					self.assertEqual(data['user']['password'], "dinosaur")
					self.assertEqual(data['user']['email'], "email@email.com")
					self.assertEqual(len(data['courses']), 0)

				db.session.delete(newUser)
				db.session.flush()

				self.assertEqual(db.session.query(User).get(1), None)

		def testNotesModel(self):
			with app.app_context():
				notetaker = User(username="Bob", password="dinosaur", email="email@email.com",
                                        admin = False)
                                db.session.add(notetaker)
                                db.session.flush()

                                newNote = Note(uid=1, stored_as="file", file_name="lecture1", owner=1, rating=5)
                                db.session.add(newNote)
                                db.session.flush()
                                self.assertEqual(db.session.query(Note).get(1).file_name, 'lecture1')

				db.session.delete(newNote)
                                db.session.flush()

                                self.assertEqual(db.session.query(Note).get(1), None)

		def testSubscriptionRelation(self):
			with app.app_context():
				professor = User(username="Bob", password="dinosaur",
					email="email@email.com", admin = True)
				db.session.add(professor)
				db.session.flush()

				student = User(username= "Susan", password = "dinsaur",
					email = "student@email.com", admin = False)
				db.session.add(student)
				db.session.flush()

				newCourse = Course(name='COMP 1010', alt_name='Computer science',
					professor = 1)
				db.session.add(newCourse)
				db.session.flush()

				student.courses.append(newCourse)
				db.session.flush()

				self.assertEqual(len(newCourse.users), 1)
				self.assertEqual(len(student.courses), 1)

				self.assertEqual(newCourse.users.pop(), student)
				db.session.flush()

				self.assertEqual(len(newCourse.users), 0)
				self.assertEqual(len(student.courses), 0)

				newCourse.users.append(student)
				db.session.flush()

				self.assertEqual(len(newCourse.users), 1)
				self.assertEqual(len(student.courses), 1)

				self.assertEqual(newCourse.users.pop(), student)
				db.session.flush()

				self.assertEqual(len(newCourse.users), 0)
				self.assertEqual(len(student.courses), 0)

		def testMessageModel(self):
			with app.app_context():
				user = User(username="Bob", password="dinosaur", email="email@email.com", admin = True)
				db.session.add(user)
				db.session.commit()

				self.assertEqual(len(User.query.all()), 1)

				newCourse = Course(name='COMP 1010', alt_name='Computer science', professor = 1)
				db.session.add(newCourse)
				db.session.commit()

				self.assertEqual(len(Course.query.all()), 1)

				message = Message(message="Hello this is message", posttime=datetime.utcnow(), courseid=newCourse.courseid, userid = user.uid)
				db.session.add(message)
				db.session.commit()

				self.assertEqual(len(Message.query.all()), 1)

				largeStr = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
				message = Message(message=largeStr, posttime=datetime.utcnow(), courseid=newCourse.courseid, userid = user.uid)
				db.session.add(message)
				db.session.commit()

				self.assertEqual(len(Message.query.all()), 2)

				# testing side loading of comments
				with app.test_client() as c:
					resp = c.get('api/messages')
					data = json.loads(resp.data)
					self.assertEqual(len(data), 2)

				with app.test_client() as c:
					resp = c.get('api/messages/1')
					data = json.loads(resp.data)
					self.assertEqual(data['message'], "Hello this is message")
					self.assertEqual(data['courseid'], 1)
					self.assertEqual(data['userid'], 1)
					self.assertEqual(data['user'], data['userid'])
					self.assertEqual(data['course'], data['courseid'])
					self.assertEqual(len(data['comments']), 0)
					self.assertEqual(len(data['comment_ids']), 0)

				comment = Comment(comment="test comment", posttime=datetime.utcnow(), messageid=2, userid = 1)
				db.session.add(comment)
				db.session.commit()

				comment = Comment(comment="test comment2", posttime=datetime.utcnow(), messageid=2, userid = 1)
				db.session.add(comment)
				db.session.commit()

				self.assertEqual(len(Comment.query.all()), 2)

				with app.test_client() as c:
					resp = c.get('api/messages/2')
					data = json.loads(resp.data)
					self.assertEqual(data['courseid'], 1)
					self.assertEqual(data['userid'], 1)
					self.assertEqual(data['user'], data['userid'])
					self.assertEqual(data['course'], data['courseid'])
					self.assertEqual(len(data['comments']), 2)
					self.assertEqual(len(data['comment_ids']), 2)

		def testCommentModel(self):
			with app.app_context():
				user = User(username="Bob", password="dinosaur", email="email@email.com", admin = True)
				db.session.add(user)
				db.session.commit()

				self.assertEqual(len(User.query.all()), 1)

				newCourse = Course(name='COMP 1010', alt_name='Computer science', professor = 1)
				db.session.add(newCourse)
				db.session.commit()

				self.assertEqual(len(Course.query.all()), 1)

				message = Message(message="Hello this is message", posttime=datetime.utcnow(), courseid=newCourse.courseid, userid = user.uid)
				db.session.add(message)
				db.session.commit()

				self.assertEqual(len(Message.query.all()), 1)

				# side loading of messages within comments is not 
				# post processed 
				with app.test_client() as c:
					resp = c.get('api/comments')
					data = json.loads(resp.data)
					self.assertEqual(len(data), 1)

				comment = Comment(comment="test comment", posttime=datetime.utcnow(), messageid=1, userid = 1)
				db.session.add(comment)
				db.session.commit()

				comment = Comment(comment="test comment2", posttime=datetime.utcnow(), messageid=1, userid = 1)
				db.session.add(comment)
				db.session.commit()

				self.assertEqual(len(Comment.query.all()), 2)

				with app.test_client() as c:
					resp = c.get('api/comments')
					data = json.loads(resp.data)
					self.assertEqual(len(data['comments']), 2)
					self.assertEqual(data['comments'][0]['id'], data['comments'][0]['commentid'])
					self.assertEqual(data['comments'][1]['id'], data['comments'][1]['commentid'])

				with app.test_client() as c:
					resp = c.get('api/comments/1')
					data = json.loads(resp.data)
					self.assertEqual(data['comment'], "test comment")
					self.assertEqual(data['messageid'], 1)
					self.assertEqual(data['userid'], 1)
					self.assertEqual(data['message']['userid'], data['userid'])

if __name__ == '__main__':
	unittest.main()
