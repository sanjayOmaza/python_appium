import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from utils.gesture_utils import GestureUtils

def get_data():
    return {"valid_phoneNumber":"9876543210","invalid_phoneNumber":"987654321","valid_otp":"0","invalid":"1"}

def setup_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "ZN4225ZZ3B"
    options.app_package = "in.vitok.dev"
    options.app_activity = "app.callpe.ui.SplashActivity"
    options.no_reset = True
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    print("App Opened Successfully")
    return driver

def login_as_streamer(driver):
    global wait
    wait = WebDriverWait(driver,20)
    data = get_data()
    valid_phone_number = data["valid_phoneNumber"]
    valid_otp = data["valid_otp"]

    wait.until(EC.element_to_be_clickable((AppiumBy.ID,"in.vitok.dev:id/customer_id"))).send_keys(valid_phone_number)
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("LOGIN AS STREAMER")'))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Send code via SMS")'))).click()
    time.sleep(3)

    for element_id in ['a1','a2','a3','a4']:
        driver.find_element(AppiumBy.ID,f'in.vitok.dev:id/{element_id}').send_keys(valid_otp)
        
    driver.find_element(AppiumBy.ID,'in.vitok.dev:id/verify').click()
    time.sleep(5)
    print("Logged into app as Streamer")

# permissions
# allow = AppPermissions()
# allow.notification_permissions()
# time.sleep(2)
# allow.camera_audio_permissions()
# time.sleep(2)
# allow.camera_audio_permissions()
# time.sleep(5)
# allow.call_permission()
# time.sleep(2)
# allow.do_not_disturb_permission()
# if AppPermissions.do_not_disturb_permission:
#     allow.do_not_disturb_permission()
# time.sleep(10)
# allow.location_permission()
# allow.camera_audio_permissions()
# time.sleep(5)


def streamer_flow():
    driver = setup_driver()
    login_as_streamer(driver)
    driver.find_element(AppiumBy.ID, 'in.vitok.dev:id/btnSwitch').click()

    # gesture = GestureUtils(driver)
    # scrolled = gesture.scroll_till_text("Last Week")
    # scrolled.click()
    # print("Scroll done")
    # time.sleep(2)

    # gesture.swipe_down(4)
    # print("swipe down done")
    # time.sleep(2)

    # gesture.swipe_Up(4)
    # print("swipe up done")
    # time.sleep(3)
    # wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Jeet")'))).click()
    
    # gesture.swipe_Left(1)
    # print("swipe left done")
    # time.sleep(10)

    # gesture.swipe_Right(1)
    # print("swipe Right done")
    # driver.press_keycode(4)
    
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Go Live")'))).click()
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Go Live")'))).click()
    print("Streamer has gone Live")

    
if __name__ == "__main__":
    streamer_flow()
