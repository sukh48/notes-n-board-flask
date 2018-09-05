App.NoteaddController = Ember.ObjectController.extend({
    actions: {
        add: function(noteName) {
            var name   = noteName;
			var cookie = document.cookie;			

			if (cookie.length != 0) {
				if(noteName.length <= 30) {
    				var cookieUID = cookie.split(';');
					var temp      = cookieUID[1].split('=');
					var userID    = temp[1];
			
    				var store = this.store;
					var notes = DS.PromiseArray.create({
						promise: this.store.find('note')
					});	

					notes.then(function() {
		                var noteAdd = store.createRecord('note', {
                    		file_name: name,
	        			    owner:     userID
        				});

            			noteAdd.save();
                   		document.getElementById('notesMsg').innerHTML = "Successfully added note";
					});
				} else {
					document.getElementById('notesMsg').innerHTML = "Course name has to be 30 or less characters long";
				}
			} else {
				document.getElementById('notesMsg').innerHTML = "Please register or signin to create a Note";
			}
        }
    }
});

App.NotesController = Ember.ArrayController.extend({
});

App.NoteController = Ember.ObjectController.extend({
	isEditing: false,   
	actions: {
		editNote: function () {
    			this.set('isEditing', true);
		},
		doneEditing: function(uid, editedText) {
			this.set('isEditing', false);
			
			var record = this.get('model');
		    record.save();
		}
	}, 
});
