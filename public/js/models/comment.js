App.Comment = DS.Model.extend({
	comment:   DS.attr('string'),
	posttime:  DS.attr('string'),
	message:  DS.belongsTo('message'),
	user: DS.belongsTo('user'),
	messageid:  DS.attr(),
	userid: DS.attr()
})