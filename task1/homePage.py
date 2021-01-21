from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import locators


class HomePage:
    time_out = 10

    def __init__(self, browser_driver):
        self.browser_driver = browser_driver
        self.wait = WDW(self.browser_driver, self.time_out)

    def close_alert_box(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, locators.alert_close_id))).click()
        # self.wait.until(EC.alert_is_present())
        # alert = self.browser_driver.alert_is_present
        # alert.dismiss()

    def click_login_link(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.login_link_xpath))).click()

    def mouse_hover(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.category_electronic_devices_xpath))).click()
        electronic_devices = self.browser_driver.find_element(By.XPATH, locators.category_electronic_devices_xpath)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.category_mobiles_xpath)))
        mobiles = self.browser_driver.find_element(By.XPATH, locators.category_mobiles_xpath)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.category_vivo_mobiles_xpath)))
        vivo_mobiles = self.browser_driver.find_element(By.XPATH, locators.category_vivo_mobiles_xpath)
        actions = ActionChains(self.browser_driver)
        actions.move_to_element(electronic_devices).move_to_element(mobiles).move_to_element(
            vivo_mobiles).click().perform()

    def add_product_to_cart(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.product_image_link_xpath)))
        self.browser_driver.find_element(By.XPATH, locators.product_image_link_xpath).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.add_to_cart_button_xpath)))
        self.browser_driver.find_element(By.XPATH, locators.add_to_cart_button_xpath).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.checkout_button_xpath)))
        self.browser_driver.find_element(By.XPATH, locators.checkout_button_xpath).click()
