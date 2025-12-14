from selenium.webdriver.support.ui import WebDriverWait
from excel.data import login_data
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginLocators


class LoginPage:
    
    global valid_phone_number
    data = login_data()
    valid_phone_number = data["valid_phone"]
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    
    def enter_phone_number(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID,LoginLocators.PHONE_NUMBER_FIELD))).send_keys(valid_phone_number)
        
    def click_on_login_as_streamer(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{LoginLocators.LOGIN_AS_STREAMER_BTN}")'))).click()

    def click_on_send_otp(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{LoginLocators.SEND_CODE_BTN}")'))).click()