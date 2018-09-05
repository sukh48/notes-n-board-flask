Feature: Logining in to the app

Scenario: Moving from the 'Home' screen to the 'Login' screen
Given I launch the app
Then I should be on the Home screen
When I navigate to Login
Then I should see a navigation bar titled "Login"

Scenario: Failing login with incorrect email
Then I should see a navigation bar titled "Login"
When I clear the text fields
When I use the keyboard to fill in the textfield marked "Email Field" with "test"
When I use the keyboard to fill in the textfield marked "Password Field" with "test"
When I attempt to login
Then I should see a navigation bar titled "Login"
Then I should see a label marked "Incorrect Email"

Scenario: Failing login with incorrect password
Then I should see a navigation bar titled "Login"
When I clear the text fields
When I use the keyboard to fill in the textfield marked "Email Field" with "guest@guest.com"
When I use the keyboard to fill in the textfield marked "Password Field" with "test"
When I attempt to login
Then I should see a navigation bar titled "Login"
Then I should see a label marked "Incorrect Password"

Scenario: Successful login
Then I should see a navigation bar titled "Login"
When I clear the text fields
When I use the keyboard to fill in the textfield marked "Email Field" with "guest@guest.com"
When I use the keyboard to fill in the textfield marked "Password Field" with "guest"
When I attempt to login
Then I should be on the Home screen

Scenario: Forgetting the user data
Then I should be on the Home screen
When I navigate to Login
Then I should see a navigation bar titled "Login"
When I clear the text fields
Then I should see a label marked "Who are you again?"