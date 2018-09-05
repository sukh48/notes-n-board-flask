from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class RegisterAndCreateCourse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://dev3.notes-n-things.tk/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_register_and_create_course(self):
        driver = self.driver
        driver.get(self.base_url + "/index.html")

        driver.find_element_by_id("courses-link").click()
        driver.find_element_by_id("create-course-button").click()
        driver.find_element_by_id("course-name-field").clear()
        driver.find_element_by_id("course-name-field").send_keys("Test 101")
        driver.find_element_by_id("alt_name-field").clear()
        driver.find_element_by_id("alt_name-field").send_keys("This is test data")
        driver.find_element_by_id("create-course-submit").click()
        
        time.sleep(3)

        try: self.assertEqual("Please register or signin to create a course", driver.find_element_by_id("coursesMsg").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.find_element_by_id("login-link").click()
        driver.find_element_by_id("email-field").clear()
        driver.find_element_by_id("email-field").send_keys("testcase@testcase.com")
        driver.find_element_by_id("password-field").clear()
        driver.find_element_by_id("password-field").send_keys("testing")
        driver.find_element_by_id("login-button").click()
        
        time.sleep(3)

        try: self.assertEqual("Wrong Email or Password was entered", driver.find_element_by_id("wrongInput").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_id("register-link").click()
        driver.find_element_by_id("new-name-field").clear()
        driver.find_element_by_id("new-name-field").send_keys("Tester")
        driver.find_element_by_id("new-email-field").clear()
        driver.find_element_by_id("new-email-field").send_keys("testcase@testcase.com")
        driver.find_element_by_id("new-password-field").clear()
        driver.find_element_by_id("new-password-field").send_keys("testing")
        driver.find_element_by_id("register-button").click()
        
        time.sleep(3)

        try: self.assertEqual("Successfully created user", driver.find_element_by_id("badInput").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_id("login-link").click()
        driver.find_element_by_id("email-field").clear()
        driver.find_element_by_id("email-field").send_keys("testcase@testcase.com")
        driver.find_element_by_id("password-field").clear()
        driver.find_element_by_id("password-field").send_keys("testing")
        driver.find_element_by_id("login-button").click()
        
        time.sleep(3)

        try: self.assertEqual("User: Tester", driver.find_element_by_id("currUser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_id("courses-link").click()
        driver.find_element_by_id("create-course-button").click()
        driver.find_element_by_id("course-name-field").clear()
        driver.find_element_by_id("course-name-field").send_keys("Testing Testing")
        driver.find_element_by_id("alt_name-field").clear()
        driver.find_element_by_id("alt_name-field").send_keys("This is a test")
        driver.find_element_by_id("create-course-submit").click()
        
        time.sleep(3)

        try: self.assertNotEqual("Successfully added course", driver.find_element_by_id("coursesMsg").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.find_element_by_id("course-name-field").clear()
        driver.find_element_by_id("course-name-field").send_keys("Test 101")
        driver.find_element_by_id("alt_name-field").clear()
        driver.find_element_by_id("alt_name-field").send_keys("This is test data")
        driver.find_element_by_id("create-course-submit").click()
        
        time.sleep(3)

        try: self.assertEqual("Successfully added course", driver.find_element_by_id("coursesMsg").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.find_element_by_id("logout-link").click()
        driver.find_element_by_id("sign-out-button").click()
        
        time.sleep(3)

        try: self.assertEqual("You have successfully signed out", driver.find_element_by_id("signout").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
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
