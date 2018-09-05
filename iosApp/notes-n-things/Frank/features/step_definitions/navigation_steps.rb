Then /^I should be on the Home screen$/ do
	%w{Courses Notes}.each do |expected_label|
		check_element_exists "view view:'UIRoundedRectButton' marked:'#{expected_label}'"
	end
end

When /^I navigate to "(.*?)"$/ do |button_name|
	touch "view:'UIRoundedRectButton' marked:'#{button_name}'"
end

Then /^I wait a bit$/ do 
	sleep 2
end