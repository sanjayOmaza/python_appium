import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from excel.data import get_data
from permissions.app_permissions import AppPermissions
from utils.gesture_utils import GestureUtils

def register_as_streamer(setup_driver):
    driver = setup_driver
    global wait,valid_phone_number,valid_otp  # this variables will be used through out the class and pass the data
    wait = WebDriverWait(driver,20)
    data = get_data()
    valid_data = data[0]
    # invalid_data = data[1]
    valid_phone_number = valid_data[0]
    valid_otp = valid_data[1]
    # invalid_phone_number = invalid_data[0]
    # invalid_otp = invalid_data[1]

    wait.until(EC.element_to_be_clickable((AppiumBy.ID,"in.vitok.dev:id/customer_id"))).send_keys(valid_phone_number)
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("LOGIN AS STREAMER")'))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Send code via SMS")'))).click()
    time.sleep(3)

    for element_id in ['a1','a2','a3','a4']:
        driver.find_element(AppiumBy.ID,f'in.vitok.dev:id/{element_id}').send_keys(valid_otp)
    
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
    wait.until(EC.element_to_be_clickable((AppiumBy.ID,"in.vitok.dev:id/customer_id"))).send_keys(valid_phone_number)
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("LOGIN AS STREAMER")'))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Send code via SMS")'))).click()
    time.sleep(3)

    for element_id in ['a1','a2','a3','a4']:
        driver.find_element(AppiumBy.ID,f'in.vitok.dev:id/{element_id}').send_keys(valid_otp)
        
    driver.find_element(AppiumBy.ID,'in.vitok.dev:id/verify').click()
    time.sleep(5)
    print("Logged into app as Streamer")

@pytest
def streamer_flow(setup_driver):
    driver = setup_driver
    login_as_streamer(driver)
    driver.find_element(AppiumBy.ID, 'in.vitok.dev:id/btnSwitch').click()

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
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Jeet")'))).click()
    
    gesture.swipe_Left(1)
    print("swipe left done")
    time.sleep(10)

    gesture.swipe_Right(1)
    print("swipe Right done")
    # driver.press_keycode(4)
    
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Go Live")'))).click()
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Go Live")'))).click()
    print("Streamer has gone Live")
    

    
if __name__ == "__main__":
    streamer_flow()
