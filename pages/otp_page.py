from excel.data import login_data
from appium.webdriver.common.appiumby import AppiumBy
from locators.otp_page_locators import OtpLocators


class OtpScreen:
    
    def __init__(self, driver):
        self.driver = driver
    
    def enter_otp(self):
        data = login_data()
        valid_otp = data["valid_otp"]
        for element_id in OtpLocators.OTP_FIELD_IDS:
            self.driver.find_element(AppiumBy.ID,f"{OtpLocators.OTP_FIELD_ID_PREFIX}{element_id}").send_keys(valid_otp)
    
    def click_on_verify(self):
        self.driver.find_element(AppiumBy.ID,OtpLocators.VERIFY_BTN).click()