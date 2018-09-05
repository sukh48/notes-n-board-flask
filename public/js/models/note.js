App.Note = DS.Model.extend({
	uid:       DS.attr(),
	stored_as: DS.attr('string'),
	file_name: DS.attr('string'),
	owner:     DS.attr(),
	rating:    DS.attr(),
	contents:  DS.attr('string')
});