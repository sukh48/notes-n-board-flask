App.MycourseController = Ember.ArrayController.extend({
    actions: {

            addMessage: function(titleText , messageText) 
            {
                    var currCourse = this.get('currCourse');        

                    var cookie = document.cookie;                   
                    if (cookie.length != 0)
                    {
                        var cookieUID = cookie.split(';');
                        var temp = cookieUID[1].split('=');
                        var userID = temp[1];
		
		                if (userID != '1'){				
                            console.log("current course: " + this.get('currCourse'));
	                        console.log("current user: "+ this.get('currCourse'));
        	                var timestamp = new Date();

                	        var messageAdd =this.store.createRecord('message', {
                                    title: titleText,
                        	        message: messageText,
                                	posttime: "12:00pm",
                                    courseid: this.get('currCourse'),
	                                userid: parseInt(userID)
        	                });

                	        messageAdd.save();
        				}else {
        					document.getElementById('errorMsg').innerHTML = "Guests can not Post";
        				}
                    }else {
                        console.log("Cannot add message: currently not logged in");
			            document.getElementById('errorMsg').innerHTML = "Guests can not Post";
                    }
            }
    }

});

App.CommentController = Ember.ObjectController.extend({
    // needs: 'message',

    actions: {

            addComment: function(commentText) {
                var comment = commentText;
                // var message = this.get('controllers.message.content');
                // var timestamp = new Date();
                // console.log(message);
                // var commentAdd =this.store.createRecord('comment', {
                //     comment: comment,
                //     posttime: "12:00pm",
                //     messageid: parseInt(message.get('id')),
                //     userid: parseInt(message.get('userid'))
                // });
                // commentAdd.save();
                // message.get('comments').addObject(commentAdd);
            }
    }
});


App.MessageController = Ember.ObjectController.extend({
    actions: {

            addComment: function(commentText) {
                var comment = commentText;
           		var message = this.get('model');
            	var timestamp = new Date();
                console.log(message);
                var commentAdd =this.store.createRecord('comment', {
                    comment: comment,
            		posttime: "12:00pm",
                    messageid: parseInt(message.get('id')),
                    userid: parseInt(message.get('userid'))
                });
                commentAdd.save();
    	        message.get('comments').addObject(commentAdd);
            }
    }
});
