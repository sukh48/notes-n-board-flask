from flask import Flask
from notesNThings.application.models.message_model import Message
import json

def api_get_many(result=None, **kw):
	print "MESSAGE: api_get_many"
	print result['objects']

	# create new key in dictionary with <modelname> and copy 
	# all objects from <objects> as defaulted by sqlAlchemy
	result['messages'] = result['objects']

	# delete all items in root dictionary except 'messages'
	# remember we already have moved the data to 'messages'
	# we are just getting rid of extra items in the dictnary 
	# which are added by sqlAlchemy
	for key in result.keys():
		if key != 'messages': 
			del result[key]

	# this adds 'ids' to the messages as ember.js does not 
	# like any different name for ids
	# essentially id == messageid here
	for test in result['messages']:
		test['id'] = test['messageid']

	# tricky part!! one to many relationship format conversion
	# create another item in root dictionary named 'comments'
	result['comments'] = []
	list = result['messages']
	for item in list:
		# since flask sqlAlchemy puts related data within each <message> item
		# need to move that to the 'comments' in the root dictionary
		result['comments'].extend(item['comments'])

		# this is just adding id field because ember doesnt like any other name
		for com in result['comments']:
			com['id'] = com['commentid']

		# cleaning up 
		del item['comments']

		# comment_ids is created within Message model
		# look at function comment_ids() in Message model
		item['comments'] = item['comment_ids']
		del item['comment_ids']

	print "result after:"
	print result

def api_get_many_pre(search_params=None, **kw):
	print "MESSAGE: api_get_many preprocessor"
	print search_params

def post_preprocessor(data=None, **kw):
	"""Accepts a single argument, `data`, which is the dictionary of
	fields to set on the new instance of the model.

	"""
	print "MESSAGE: POST  preprocessor"
	print data
	#data = data['user'].copy()
	data['title'] = data['message']['title']
	data['messagetxt'] = data['message']['message']
	data['posttime'] = data['message']['posttime']
	data['userid'] = data['message']['userid']
	data['courseid'] = data['message']['courseid']

	del data['message']
	data['message'] = data['messagetxt']
	del data['messagetxt']
	print data

	pass

def post_postprocessor(result=None, **kw):
	"""Accepts a single argument, `result`, which is the dictionary
	representation of the created instance of the model.

	"""
	print "MESSAGE: result['comments']POST postprocessor"
	result['message'] = result.copy()
	for key in result.keys():
		if key != 'message': 
			del result[key]

	result['message']['id'] = result['message']['messageid']
	print result	
	pass

def create_message_api(restless_manager):
	# Create API endpoints, which will be available at /api/<tablename> by
	# default. Allowed HTTP methods can be specified as well.
	restless_manager.create_api(
		Message, 

		# these are the names of methods that are defined in 
		# the Message model
		include_methods=['course', 'user', 'comment_ids'], 
		methods=['GET', 'POST', 'DELETE', 'PUT'], 
		url_prefix='/api',
		collection_name='messages',
		postprocessors={
	        'GET_MANY': [api_get_many],
	        #'GET_SINGLE' : [api_get_many],
	        'POST': [post_postprocessor]
	    },
	    preprocessors={
	    	'GET_MANY': [api_get_many_pre],
	        'POST': [post_preprocessor]
	    }
	)