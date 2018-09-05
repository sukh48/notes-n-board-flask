App.Router.map(function() {
	this.resource('home', { path : '/'}, function() {
		this.resource('mycourse', { path : ':course_id' } );
	});

	this.resource('messages', function() {
		this.resource('message', { path : ':message_id' });
	});

	this.resource('notes', function() {
		this.resource('note', { path : ':note_id' } );
		this.resource('noteadd');
	});

	this.resource('courses', function() {
		this.resource('course', { path : ':course_id' } );
		this.resource('courseadd');
	});

	this.resource('users', function() {
		this.resource('user', { path : ':user_id' } );
	});

	this.resource('login');
	this.resource('logout');
	this.resource('createaccount');
});

App.LogoutRoute = Ember.Route.extend({
	model: function() {
	return Em.Object.create({});
	}
 });

App.LoginRoute = Ember.Route.extend({
	model: function() {
	return Em.Object.create({});
	}
 });

App.CreateaccountRoute = Ember.Route.extend({
	model: function() {
		//the model for this route is a new empty Ember.Object
		return Em.Object.create({});
	}
 });

App.CourseaddRoute = Ember.Route.extend({
  	model: function(){
    	// the model for this route is a new empty Ember.Object
    	return Em.Object.create({});
  	}
 });

App.MycourseRoute = Ember.Route.extend({
  	model: function(params) {
  		this.set('currCourse', params.course_id);

    	var string = '{"filters":[{"name":"courseid","op":"eq","val":'+params.course_id+'}]}'
    	return this.store.filter('message', { q: string }, function(message) {
      		return message.get('courseid')==params.course_id;
    	});
  	},

	setupController: function (controller, model) 
  	{
  		controller.set('model', model);
     	controller.set('currCourse', this.get('currCourse'));
  	}
 });

App.HomeRoute = Ember.Route.extend(
{
	model: function() {
		var userID = 1;	// guest user
		var cookie = document.cookie;                   
	    if (cookie.length != 0)
	    {
            var cookieUID = cookie.split(';');
            var temp = cookieUID[1].split('=');
            var userID = temp[1];
            console.log("userID: " + userID);
	    }

	 	return this.store.find('user', userID);  
	}

});

App.MessagesRoute = Ember.Route.extend(
{
	model: function() {
		return this.store.find('message');
	}
});

App.MessageRoute = Ember.Route.extend({
	model: function(params) {
		return this.store.find('message', params.message_id);
	}
});

App.UsersRoute = Ember.Route.extend({
	model: function() {
		return this.store.find('user');
	}
});

App.UserRoute = Ember.Route.extend({
	model: function(params) {
		return this.store.find('user', params.user_id);
	}
});

App.CoursesRoute = Ember.Route.extend({
	model: function() {
		return this.store.find('course');
	}
});

App.CourseRoute = Ember.Route.extend({
	model: function(params) {
		return this.store.find('course', params.course_id);
	},

	setupController: function (controller, model) 
  	{
  		controller.set('model', model);
     	controller.set('currUser', this.store.find('user', 1));
  	}
});

App.NotesRoute = Ember.Route.extend({
	model: function() {
		return this.store.find('note');
	}
});

App.NoteRoute = Ember.Route.extend({
	model: function(params) {
		return this.store.find('note', params.note_id);
	}
})

App.NoteaddRoute = Ember.Route.extend({
  	model: function(){
    	// the model for this route is a new empty Ember.Object
    	return Em.Object.create({});
  	}
 });

