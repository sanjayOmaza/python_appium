from appium import webdriver
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "ZN4225ZZ3B"
options.app_package = "in.vitok.dev"
options.app_activity = "app.callpe.ui.SplashActivity"
options.no_reset = True   # optional: don't reset app data, keeps app state

def open_app(driver):
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )
    return driver