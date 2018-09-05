When /^I navigate to Login$/ do 
	touch "view:'UINavigationButton' marked:'Login'"
	sleep 2
end

When /^I clear the text fields$/ do
	sleep 2
	touch "view:'UIButton' marked:'Forget Me'"
	sleep 2
end

When /^I attempt to login$/ do
	sleep 2
	touch "view:'UIButton' marked:'Submit'"
	sleep 2
end

When /^I use the keyboard to fill in the textfield marked "([^\\"]*)" with "([^\\"]*)"$/ do |text_field_mark, text_to_type|
    text_field_selector =  "view marked:'#{text_field_mark}'"
    check_element_exists( text_field_selector )
    touch( text_field_selector )
    frankly_map( text_field_selector, 'setText:', text_to_type )
    frankly_map( text_field_selector, 'endEditing:', true )
end

Then /^I should see a label marked "(.*?)"$/ do |label_name|
	check_element_exists "view view:'UILabel' marked:'#{label_name}'"
end