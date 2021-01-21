from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import locators


class LoginPage:
    time_out = 10

    def __init__(self, browser_driver):
        self.browser_driver = browser_driver
        self.wait = WDW(self.browser_driver, self.time_out)

    def login(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.username_input_xpath)))
        self.browser_driver.find_element(By.XPATH, locators.username_input_xpath).send_keys('03346398431')
        self.browser_driver.find_element(By.XPATH, locators.password_input_xpath).send_keys('kashi4oll')
        self.browser_driver.find_element(By.XPATH, locators.login_button_xpath).click()
