from selenium import webdriver
from homePage import HomePage
from loginPage import LoginPage

import locators


driver_path = '..\driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)


def set_up():
    driver.maximize_window()
    driver.get(locators.home_page_url)


set_up()
home_page = HomePage(driver)
login_page = LoginPage(driver)
home_page.close_alert_box()
home_page.click_login_link()
login_page.login()
home_page.mouse_hover()
home_page.add_product_to_cart()
driver.quit()
