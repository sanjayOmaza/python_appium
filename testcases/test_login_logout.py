import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from excel.data import login_data
from locators.home_page_locators import HomepageLocators
from locators.login_page_locators import LoginLocators
from locators.otp_page_locators import OtpLocators
from permissions.app_permissions import AppPermissions
from utils.gesture_utils import GestureUtils

def register_as_streamer(setup_driver):
    driver = setup_driver
    global wait,valid_phone_number,valid_otp  # this variables will be used through out the class and pass the data
    wait = WebDriverWait(driver,20)
    data = login_data()
    valid_phone_number = data["valid_phone"]
    valid_otp = data["valid_otp"]
    wait.until(EC.element_to_be_clickable((AppiumBy.ID,LoginLocators.PHONE_NUMBER_FIELD))).send_keys(valid_phone_number)
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("{LoginLocators.LOGIN_AS_STREAMER_BTN}")'))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("{LoginLocators.SEND_CODE_BTN}")'))).click()
    time.sleep(3)

    for element_id in OtpLocators.OTP_FIELD_IDS:
        driver.find_element(AppiumBy.ID,f"{OtpLocators.OTP_FIELD_ID_PREFIX}{element_id}").send_keys(valid_otp)
    
    # Need to handle the sign up process

def allow_permissions():
    allow = AppPermissions()
    allow.notification_permissions()
    time.sleep(2)
    allow.camera_audio_permissions()
    time.sleep(2)
    allow.camera_audio_permissions()
    time.sleep(5)
    allow.call_permission()
    time.sleep(2)
    allow.do_not_disturb_permission()
    if AppPermissions.do_not_disturb_permission:
        allow.do_not_disturb_permission()
    time.sleep(10)
    allow.location_permission()
    allow.camera_audio_permissions()
    time.sleep(5)

def login_as_streamer(setup_driver):
    driver = setup_driver
    wait = WebDriverWait(driver,20)
    wait.until(EC.element_to_be_clickable((AppiumBy.ID,LoginLocators.PHONE_NUMBER_FIELD))).send_keys(valid_phone_number)
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("{LoginLocators.LOGIN_AS_STREAMER_BTN}")'))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("{LoginLocators.SEND_CODE_BTN}")'))).click()
    time.sleep(3)
    
    for element_id in OtpLocators.OTP_FIELD_IDS:
        driver.find_element(AppiumBy.ID,f"{OtpLocators.OTP_FIELD_ID_PREFIX}{element_id}").send_keys(valid_otp)
       
    driver.find_element(AppiumBy.ID,OtpLocators.VERIFY_BTN).click()
    time.sleep(5)
    print("Logged into app as Streamer")

@pytest
def streamer_flow(setup_driver):
    driver = setup_driver
    login_as_streamer(driver)
    driver.find_element(AppiumBy.ID, HomepageLocators.ONLINE_BTN).click()

    gesture = GestureUtils(driver)
    scrolled = gesture.scroll_till_text("Last Week")
    scrolled.click()
    print("Scroll done")
    time.sleep(2)

    gesture.swipe_down(4)
    print("swipe down done")
    time.sleep(2)

    gesture.swipe_Up(4)
    print("swipe up done")
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{HomepageLocators.STREAMER_NAME}")'))).click()
    
    gesture.swipe_Left(1)
    print("swipe left done")
    time.sleep(10)

    gesture.swipe_Right(1)
    print("swipe Right done")
    # driver.press_keycode(4)
    
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("{HomepageLocators.GO_LIVE_BTN}")'))).click()
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("{HomepageLocators.GO_LIVE_BTN}")'))).click()
    print("Streamer has gone Live")
    

    
if __name__ == "__main__":
    streamer_flow()
