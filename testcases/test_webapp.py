from appium import webdriver
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "ZN4225ZZ3B"
options.automation_name = "UiAutomator2"
options.browser_name = "Chrome"

# Enable automatic Chromedriver download
options.set_capability("chromedriver_autodownload", True)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Example navigation
driver.get("https://www.google.com")
print(driver.title)

driver.quit()
