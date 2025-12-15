import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.otp_page import OtpScreen
from pages.signup_pages import SignupPage
from utils.gesture_utils import GestureUtils

def login_as_streamer(setup_driver):
    loginPage = LoginPage(setup_driver)
    otpScreen = OtpScreen(setup_driver)

    loginPage.enter_phone_number()
    loginPage.click_on_login_as_streamer()
    loginPage.click_on_send_otp()
    otpScreen.enter_otp()
    otpScreen.click_on_verify()
    
def register_as_streamer(setup_driver):
    signupPage = SignupPage(setup_driver)
    signupPage.select_date()
    signupPage.select_month()
    signupPage.select_year()
    time.sleep(5)
    signupPage.click_on_next()
    signupPage.select_gender_female()
    signupPage.click_on_next()
    time.sleep(5)
    signupPage.enter_nick_name()
    signupPage.click_on_next()
    time.sleep(5)
    signupPage.select_language_hindi()
    signupPage.select_language_english()
    signupPage.click_on_next()
    time.sleep(3)
    # signupPage.enter_referral_code()
    signupPage.click_on_skip()
    time.sleep(3)
    signupPage.select_gallery_photo_proof()
    signupPage.click_on_next()
    time.sleep(3)
    signupPage.choose_gallery_photo_profile()
    signupPage.click_on_next()
    time.sleep(3)
    signupPage.upload_profile_pic()
    signupPage.choose_gallery_photo_profile()
    signupPage.click_on_next()
    time.sleep(3)
    signupPage.open_camera()
    signupPage.tap_on_record()
    time.sleep(10)
    signupPage.click_on_next()
    print("Signed Up successfully")
    

def test_register_as_streamer(setup_driver):
    login_as_streamer(setup_driver)
    time.sleep(5)
    
    # Need to handle the sign up process

def test_login_as_streamer(setup_driver):
    login_as_streamer(setup_driver)

# def test_streamer_flow(setup_driver):
#     homePage = HomePage(setup_driver)
#     login_as_streamer(setup_driver)
    
#     gesture = GestureUtils(setup_driver)
#     scrolled = gesture.scroll_till_text("Last Week")
#     scrolled.click()
#     print("Scroll done")
#     time.sleep(2)

#     gesture.swipe_down(4)
#     print("swipe down done")
#     time.sleep(2)

#     gesture.swipe_Up(1)
#     print("swipe up done")
#     time.sleep(3)
    
#     homePage.click_on_streamer()
    
#     gesture.swipe_Left(1)
#     print("swipe left done")
#     time.sleep(10)

#     gesture.swipe_Right(1)
#     print("swipe Right done")
#     time.sleep(5)
    
# def test_go_live(setup_driver):
#     # login_as_streamer(setup_driver)
#     homePage = HomePage(setup_driver)
#     homePage.go_online()
#     homePage.go_live()