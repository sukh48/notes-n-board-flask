module("Testing the course controller", {
	setup: function() {
		App.reset();
		App.injectTestHelpers();

		controller = App.__container__.lookup('controller:course');
                model = App.Course;
                controller.set('model', model);

		App.Course.FIXTURES = [{
			alt_name:	"This is test data",
			courseid:	1,
			name:		"Test 1010",
			professor:	1
		}];

		App.User.FIXTURES = [{
			admin:		true,
			email:		"testing@tests.test",
			password:	"dinosaur",
			uid:		1,
			username:	"tester"
		}];

		App.Note.FIXTURES = [{
			file_name:	"lecture1",
			owner:		1,
			rating:		5,
			stored_as:	"file",
			uid:		1
		}];

		App.Message.FIXTURES=[{
			course:		1,
			courseid:	1,
			message:	"Hello world",
			messageid:	1,
			posttime:	"2001-04-10T00:00:00",
			user:		1,
			userid:		1,
			comments:	[]
		}];

	},

	teardown: function(){
		controller = null;
		model = null;
	}
});


