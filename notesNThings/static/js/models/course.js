App.Course = DS.Model.extend({
	name:      DS.attr('string'),
	alt_name:  DS.attr('string'),
	professor: DS.attr(),
	users: DS.hasMany('user'),
})
