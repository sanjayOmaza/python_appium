from appium import webdriver
from appium.options.android import UiAutomator2Options
# from appium.webdriver.appium_service import AppiumService

import pytest
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item,"rep"+rep.when,rep)
#     return rep

@pytest.fixture(scope='session')
def setup_driver():
    # appium_service = AppiumService()
    # appium_service.start()
    
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "ZN4225ZZ3B"
    options.app_package = "in.vitok.dev"
    options.app_activity = "app.callpe.ui.SplashActivity"
    options.no_reset = True
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    print("App Opened Successfully")
    yield driver
    driver.quit()
    # appium_service.stop()

# @pytest.fixture
# def log_on_failures(request,setup_driver):
#     yield
#     item = request.node
#     driver = setup_driver
#     if item.rep_call.failed:
#         driver.get_screenshot_as_png()