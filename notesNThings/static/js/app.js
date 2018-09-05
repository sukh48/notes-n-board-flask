window.App = Ember.Application.create();

App.Store = DS.Store.extend({
    revision: 12,
    adapter: DS.RESTAdapter.reopen({
        namespace: 'api'
    })
});

