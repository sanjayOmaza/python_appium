from appium.webdriver.common.appiumby import AppiumBy

class AppPermissions:
    
    def notification_permissions(driver):
        notificationpermission = driver.find_element(AppiumBy.ID,'com.android.permissioncontroller:id/permission_allow_button')
        notificationpermission.click()
    
    def camera_audio_permissions(driver):
        cameraAndAudioPermission = driver.find_element(AppiumBy.ID,'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        cameraAndAudioPermission.click()
        
    def call_permission(driver):
        callPermission = driver.find_element(AppiumBy.ID,'com.android.permissioncontroller:id/permission_allow_button')
        callPermission.click()
        
    def do_not_disturb_permission(driver):
        defaultAppPermission = driver.find_element(AppiumBy.ID,'android:id/button2')
        defaultAppPermission.click()
        
    def location_permission(driver):
        locationPermission = driver.find_element(AppiumBy.ID,'in.vitok.dev:id/grantButton')
        locationPermission.click()