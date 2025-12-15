import time
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from excel.data import login_data
from locators.signup_pages_locators import SignupLocators

class SignupPage:
    
    global DOB_date,DOB_month,DOB_year,nick_name,referral_code
    data = login_data()
    DOB_date = data["DOB_date"]
    DOB_month = data["DOB_month"]
    DOB_year = data["DOB_year"]
    nick_name = data["nick_name"]
    referral_code = data["referral_code"]
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    
    def select_date(self):
        self.driver.find_element(AppiumBy.XPATH, SignupLocators.DATE_PICKER).send_keys(DOB_date)
        
    def select_month(self):
        self.driver.find_element(AppiumBy.XPATH, SignupLocators.MONTH_PICKER).send_keys(DOB_month)
    
    def select_year(self):
        self.driver.find_element(AppiumBy.XPATH, SignupLocators.YEAR_PICKER).send_keys(DOB_year)
        
    def click_on_next(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.NEXT_BTN).click()
        
    def select_gender_female(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.GENDER_FEMALE).click()
    
    def select_gender_male(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.GENDER_MALE).click()
        
    def enter_nick_name(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.NICK_NAME_FIELD).send_keys(nick_name)
        
    def select_language_hindi(self):
        self.driver.find_element(AppiumBy.XPATH,SignupLocators.LANGUAGE_HINDI).click()
      
    def select_language_english(self):
        self.driver.find_element(AppiumBy.XPATH,SignupLocators.LANGUAGE_ENGLISH).click()
        
    def enter_referral_code(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.REFERRAL_CODE).send_keys(referral_code)
    
    def click_on_skip(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.SKIP_BTN).click()
      
    def select_gallery_photo_proof(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.PROOF_GALLERY_BTN).click()
        self.driver.find_element(AppiumBy.XPATH, SignupLocators.SELECT_PHOTO_FROM_GALLERY_PROOF).click()
        
    def select_camera_image_proof(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.PROOF_CAMERA_BTN).click()
        self.driver.find_element(AppiumBy.ID, SignupLocators.SELECT_PHOTO_FROM_GALLERY_PROOF).click()
        
    def click_on_remove(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.REMOVE_BTN).click()
        
    def upload_profile_pic(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.UPLOAD_PROFILE).click()
        
    def choose_gallery_photo_profile(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.PROFILE_GALLERY_OPTION).click()
        self.driver.find_element(AppiumBy.XPATH, SignupLocators.SELECT_PHOTO_FROM_GALLERY_PROFILE).click()
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{SignupLocators.DONE_BTN}")'))).click()

    def choose_camera_image_profile(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.PROFILE_CAMERA_OPTION).click()
        self.driver.find_element(AppiumBy.ID, SignupLocators.SELECT_IMAGE_FROM_CAMERA_PROFILE).click()
        
    def open_camera(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.OPEN_CAMERA).click()
        
    def tap_on_record(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.TAP_ON_RECORD).click()
        time.sleep(15)
        
    def remove_audition_video(self):
        self.driver.find_element(AppiumBy.ID, SignupLocators.REMOVE_AUDITION_VIDEO).click()
    
    
        
    
     
       
    
       
    
     
        
        