import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestUnicornWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_login_unicorn(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "username")))
        elemUser = driver.find_element(By.NAME, "username")
        elemUser.send_keys("bilgekagan")

        elemPass = driver.find_element(By.NAME, "password")
        elemPass.send_keys("12345")

        elemLogin = driver.find_element(By.NAME, "login")
        elemLogin.click()

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")))

        alertMesg = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")

        assert "ERROR: INCORRECT USERNAME OR PASSWORD." in alertMesg.text

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
