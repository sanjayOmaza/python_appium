import time
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HomepageLocators
from permissions.app_permissions import AppPermissions

class HomePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    
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
    
    def go_online(self):
        self.driver.find_element(AppiumBy.ID, HomepageLocators.ONLINE_BTN).click()
        
    def click_on_streamer(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{HomepageLocators.STREAMER_NAME}")'))).click()
    
    def go_live(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{HomepageLocators.GO_LIVE_BTN}")'))).click()
    