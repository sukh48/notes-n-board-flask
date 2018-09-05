from flask import Flask
from notesNThings.application.models.comment_model import Comment
import json

def api_get_many(result=None, **kw):
	print "COMMENT: api_get_many"
	print result['objects']
	result['comments'] = result['objects']
	for key in result.keys():
		print key 
		if key != 'comments': 
			del result[key]
	for test in result['comments']:
		test['id'] = test['commentid']
	print result
	pass

def post_preprocessor(data=None, **kw):
	print "COMMENT: POST  preprocessor"
	print data
	data['commenttxt'] = data['comment']['comment']
	data['posttime'] = data['comment']['posttime']
	data['userid'] = data['comment']['userid']
	data['messageid'] = data['comment']['messageid']
	del data['comment']
	data['comment'] = data['commenttxt']
	del data['commenttxt']
	print data
	pass

def post_postprocessor(result=None, **kw):
	print "COMMENT: POST postprocessor"
	result['comment'] = result.copy()
	for key in result.keys():
		if key != 'comment': 
			del result[key]

	del result['comment']['message']
	result['comment']['id'] = result['comment']['commentid']
	print result	
	pass

def create_comment_api(restless_manager):
	# Create API endpoints, which will be available at /api/<tablename> by
	# default. Allowed HTTP methods can be specified as well.
	restless_manager.create_api(
		Comment,  
		methods=['GET', 'POST', 'DELETE', 'PUT'], 
		url_prefix='/api',
		collection_name='comments',
		postprocessors={
	        'GET_MANY': [api_get_many],
	        'POST': [post_postprocessor],
	    },
	    preprocessors={
	        'POST': [post_preprocessor],
	    }
	)
