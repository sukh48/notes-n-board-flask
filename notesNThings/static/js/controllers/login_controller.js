App.LoginController = Ember.ObjectController.extend({
	
        actions: {
                login: function(email, password) {
                        var email = email;
                        var password = password;
						var foundUser = new Boolean();
						foundUser = false;
			                       
						var users = DS.PromiseArray.create({
							promise:  this.store.find('user')
						});
							
						users.then(function() {
							var user = "";
							var tempEmail = "";				

							user = users.get('firstObject');
							while (!foundUser && user != null){
							
								tempEmail = user.get('email');
								tempPass = user.get('password');

								tempPass = tempPass.trim();

								if (email.localeCompare(tempEmail) == 0 && password.localeCompare(tempPass) == 0){
									foundUser = true;
								}
								else {
									user = users.popObject();
								}										
							}
							if (user != null){
								
								document.cookie = "username=" + user.get('username'); "path=/";
								document.cookie = "userID=" + user.get('id'); "path=/";
								document.getElementById("wrongInput").innerHTML = "Successfully logged in";					
								document.getElementById("currUser").innerHTML = user.get('username');
								document.getElementById('login').style.display = "none";
								document.getElementById('register').style.display = "none";
								document.getElementById('logout').style.display = "inline";
								document.getElementById('wrongInput').style.display = "inline";
								//document.getElementById('currUser').style.display = "inline";
							}
							else {
								document.getElementById("wrongInput").innerHTML="<li>Wrong Email or Password was entered</li>";
							}

						});
                }
        }
});

