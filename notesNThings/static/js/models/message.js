App.Message = DS.Model.extend({
	title: DS.attr('string'),
	message: DS.attr('string'),
	posttime:  DS.attr('string'),
	course:  DS.belongsTo('course'),
	user: DS.belongsTo('user'),
	comments: DS.hasMany('comment'),
	courseid:  DS.attr(),
	userid: DS.attr()
})