App.UserController = Ember.ObjectController.extend({
	isEditing: false,

  	actions: {
		edit: function() {
			this.set('isEditing', true);
		},

		doneEditing: function() {
			this.set('isEditing', false);
			
			var record = this.get('model');
		    record.save();
		}                
	}
});

App.CreateaccountController = Ember.ObjectController.extend({

	actions: {
		add: function(name, email, password){
			var name = name;
			var email = email;
			var password = password;			
			var foundUser = new Boolean();
			foundUser = false;
			
			var store = this.store;
				
		        var users = DS.PromiseArray.create({
                                promise:  this.store.find('user')
                        });
			
                        users.then(function() {
                                var user = "";
                                var tempEmail = "";

                                user = users.get('firstObject');
                                while (!foundUser && user != null){
					tempUser = user.get('username');
                                        tempEmail = user.get('email');
                                        
                                        if (name.localeCompare(tempUser) == 0 || email.localeCompare(tempEmail) == 0){
 				                foundUser = true;
                                        }
                                        else {
                                                user = users.popObject();
                                        }
                                }
			        if (foundUser){
        	                        document.getElementById('badInput').innerHTML = "<li>Username or email are already being used</li>";
	                        }
                        	else {
                	                document.getElementById('badInput').innerHTML = "<li>Successfully created user</li>";
        	        		
					var userAdd = store.createRecord('user', {
                                		username: name,
	                        	        email: email,
        		                        password: password,
		                                admin: false
		                        });   
					userAdd.save();
			     }
                        });						
       		}
	}
});
