# import time
# from appium.webdriver.common.appiumby import AppiumBy
# from permissions.app_permissions import AppPermissions

# class LoginPass:
    
#     def __init__(self,driver):
#         self.driver = driver
        
#     def login_success(self):
#         self.driver.find_element(AppiumBy.ID,"in.vitok.dev:id/customer_id").send_keys("9876543213")
#         self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("LOGIN AS STREAMER")').click()
#         self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Send code via SMS")').click()
#         time.sleep(3)
#         self.driver.find_element(AppiumBy.ID,'in.vitok.dev:id/a1').send_keys("0")
#         self.driver.find_element(AppiumBy.ID,'in.vitok.dev:id/a2').send_keys("0")
#         self.driver.find_element(AppiumBy.ID,'in.vitok.dev:id/a3').send_keys("0")
#         self.driver.find_element(AppiumBy.ID,'in.vitok.dev:id/a4').send_keys("0")
#         self.driver.find_element(AppiumBy.ID,'in.vitok.dev:id/verify').click()
#         print("App Opened Successfully")
#         time.sleep(5)
        
#     def permission_access(self):
#         allow = AppPermissions()
#         allow.notification_permissions()
#         time.sleep(2)
#         allow.camera_audio_permissions()
#         time.sleep(5)
#         allow.call_permission()
#         time.sleep(2)
#         allow.do_not_disturb_permission()
#         if AppPermissions.do_not_disturb_permission:
#             allow.do_not_disturb_permission()
        
#         time.sleep(10)
#         allow.location_permission()
#         allow.camera_audio_permissions()
