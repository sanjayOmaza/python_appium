from appium.webdriver.common.appiumby import AppiumBy

class GestureUtils:
    
    def __init__(self,driver):
        self.driver = driver

    def scroll_till_text(self,text):
        try:
            return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("{}"));'.format(text))
        except NoSuchElementException:  # type: ignore
            raise Exception(f"Element containing text '{text}' not found!")
            
    def scroll_till_resource_id(self,resource_id):
        try:
            return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceID("{}));'.format(resource_id))
        except NoSuchElementException: # type: ignore
            raise Exception(f"Element conataining resourceID '{resource_id}' not found!")
    
    def swipe_down(self,howManySwipes):
        for i in range(1, howManySwipes+1):
            self.driver.swipe(500,880,500,600,1000)
        
    def swipe_Up(self,howManySwipes):
        for i in range(1, howManySwipes+1):
            self.driver.swipe(500,600,500,800,1000)
            
    def swipe_Left(self, howManySwipes):
        for i in range(1, howManySwipes+1):
            self.driver.swipe(500,800,300,800,1000)
            
    def swipe_Right(self,howManySwipes):
        for i in range(1, howManySwipes+1):
            self.driver.swipe(400,800,600,800,1000)