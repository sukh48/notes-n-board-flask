from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class TryToCreateCourseWithTooLongName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://dev3.notes-n-things.tk/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_try_to_create_course_with_too_long_name(self):
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_id("login-link").click()
        driver.find_element_by_id("email-field").clear()
        driver.find_element_by_id("email-field").send_keys("david@david.com")
        driver.find_element_by_id("password-field").clear()
        driver.find_element_by_id("password-field").send_keys("dinosaur")
        driver.find_element_by_id("login-button").click()
        driver.find_element_by_id("courses-link").click()
        driver.find_element_by_id("create-course-button").click()
        driver.find_element_by_id("course-name-field").clear()
        driver.find_element_by_id("course-name-field").send_keys("Comp123456789")
        driver.find_element_by_id("alt_name-field").clear()
        driver.find_element_by_id("alt_name-field").send_keys("too long of course name")
        driver.find_element_by_id("create-course-submit").click()
        self.assertEqual("Course name has to be 9 or less characters long", driver.find_element_by_id("coursesMsg").text)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
