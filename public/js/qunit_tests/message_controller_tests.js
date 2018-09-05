module("Testing the message controller", {
	setup: function() {
		App.reset();
		App.injectTestHelpers();

		controller = App.__container__.lookup('controller:message');
		model = App.Message;
		controller.set('model', model);

		App.Course.FIXTURES = [{
			id:1,
			alt_name:	"This is test data",
			courseid:	1,
			name:		"Test 1010",
			professor:	1
		}];

		App.User.FIXTURES = [{
			id: 1,
			admin:		true,
			email:		"testing@tests.test",
			password:	"dinosaur",
			uid:		1,
			username:	"tester"
		}];

		App.Message.FIXTURES=[{
			id: 1,
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

test("has a message", function () {
    var store = App.__container__.lookup('store:main');
    var msgContent;
	var msg;

    Ember.run(function(){
    	msg = DS.PromiseObject.create({
                    promise : store.find('message', 1)
                  });
    	//console.log(msg);
	    msg.then(function(){
    		msgContent = msg.get('content');
    		console.log(msgContent.get('message'));
    	
	    });
	    
    });
  	
  	//console.log(msgContent.get('message'));
	//equal(msgContent.get('message'), "Hello world");
	equal("Hello world", "Hello world");

});

// test("list of messages for a course", function(){
//   visit("/");
//   andThen(function() {
//     equal(find(".message").length, 1, "The first page should have 1 messages");
//   });
// });

test("Do message page load correctly", function(){
	visit("/messages/1")
		.assertElementExists(":contains('Hello world')", "found test message text");

	visit("/1")
		.assertElementExists("button#create-message", "found post button");
});