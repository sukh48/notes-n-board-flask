module("Testing the templates", {
	setup: function() {
		App.reset();
		App.injectTestHelpers();

		$.removeCookie("userID");
                $.removeCookie("username");

		App.Course.FIXTURES = [{
			alt_name:	"This is test data",
			courseid:	1,
			id :		1,
			name:		"Test 1010",
			professor:	1
		}];

		App.User.FIXTURES = [{
			admin:		true,
			email:		"testing@tests.test",
			id:		1,
			password:	"dinosaur",
			uid:		1,
			username:	"tester"
		}];

		App.Note.FIXTURES = [{
			file_name:	"lecture1",
			id:		1,
			owner:		1,
			rating:		5,
			stored_as:	"file",
			uid:		1
		}];

		App.Message.FIXTURES=[{
			course:		1,
			courseid:	1,
			id:		1,
			message:	"Hello world",
			messageid:	1,
			posttime:	"2001-04-10T00:00:00",
			user:		1,
			userid:		1,
			comments:	[]
		}];

		App.Comment.FIXTURES=[{
			comment:	"Test comment",
			commentid:	1,
			messageid:	1,
			posttime:	"2014-03-26T12:00:00",
			user:		1
		}];

	}
});

test("App Instantiation", function() {
	equal(
		App.constructor, Ember.Application,
		'App is an Ember App!'
	);
});

test("Does the homepage work correctly", function() {
	visit("/")
		.assertElementExists("ul#home-sidebar", "found homepage course sidebar");

	visit("/")
		.assertElementExists("h1#home-header", "found homepage header");

});

test("Does the notes page work correctly", function() {

	visit("/notes")
		.assertElementExists("a#create-note-button", "found create note button");

	visit("/notes")
		.assertElementExists("div#notes-sidebar", "found notes sidebar");

	visit("/notes")
		.assertElementExists("h1#notes-header", "found notes header");

});

test("Does the courses page work correctly", function(){

	visit("/courses")
		.assertElementExists("ul#courses-sidebar", "found courses sidebar");

	visit("/courses")
		.click("a[href$=\"courseadd\"]")
		.assertElementExists("div#course-container", "add course form successfully loads");

	visit("/courses")
		.assertElementExists("h1#courses-header", "found courses header");
});

test("Does the login page work correctly", function(){

	visit("/login")
		.assertElementExists("form#signin-form", "found login form");

	visit("/login")
		.assertElementExists("input#email-field", "found email field");

	visit("/login")
		.assertElementExists("input#password-field", "found password field");

	visit("/login")
		.assertElementExists("button#login-button", "found signin button");

	visit("/login")
		.assertElementExists("a#create-account-button", "found register link");

});

test("Does the registration page load correctly", function(){
	visit("/createaccount")
		.assertElementExists("form#register-form", "found register form");
	visit("/createaccount")
		.assertElementExists("input#new-name-field", "found new name field");
	visit("/createaccount")
		.assertElementExists("input#new-email-field", "found new email field");
	visit("/createaccount")
		.assertElementExists("input#new-password-field", "found new password field");
	visit("/createaccount")
		.assertElementExists("button#register-button", "found register button");
});

test("Does the users page load correctly", function(){

	visit("/users")
		.assertElementExists("ul#users-sidebar", "found users sidebar");

	visit("/users")
		.assertElementExists("h1#users-header", "found users header");

});

test("Does the message board page load correctly", function(){
	visit("/messages")
		.assertElementExists(":contains('Messages')", "found messages header");

	visit("/messages")
		.assertElementExists("ul#messages-sidebar", "found messages sidebar");
});

test("Do individual course pages load correctly", function(){
	visit("/courses/1")
		.assertElementExists(":contains('Test 1010')", "found test course text");

	visit("/courses/1")
		.assertElementExists("button#subscribe-button", "found subscribe button");
});

test("Do individual note pages load correctly", function(){
	visit("/notes/1")
		.assertElementExists(":contains('Test title:lecture1')", "fount test note text");
});

test("Do individual user pages load correctly", function(){
	visit("/users/1")
		.assertElementExists(":contains('username: tester')", "found individual user");
});

test("Do individual message pages load correctly", function(){
	visit("/messages/1")
		.assertElementExists(":contains('Hello world')", "found individual message");
});

