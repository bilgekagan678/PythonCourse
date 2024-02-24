import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestUnicornWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_login_unicorn(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")

        elemUser = driver.find_element(By.NAME, "username")
        elemUser.send_keys("bilgekagan")

        elemPass = driver.find_element(By.NAME, "password")
        elemPass.send_keys("12345")

        elemLogin = driver.find_element(By.NAME, "login")
        elemLogin.click()

        assert "INCORRECT USERNAME OR PASSWORD." not in driver.page_source
        # assert "INCORRECT USERNAME OR PASSWORD." in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
