// put app in qunit-fixture
window.App = Ember.Application.create({
  rootElement: '#qunit-fixture'
});

App.Store = DS.Store.extend({
    revision: 12,
    adapter: DS.FixtureAdapter.reopen({
        namespace: 'api'
    })
});

Ember.Test.registerHelper('assertElementExists', function(app, selector, message){
	return wait()
		.find(selector)
		.then(function(elements){
			notEqual(elements.length, 0, message);
		});
});

// turn on testing mode
window.App.setupForTesting();
