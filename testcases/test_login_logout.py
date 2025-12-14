from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.otp_page import OtpScreen
# from utils.gesture_utils import GestureUtils

def login_as_streamer(setup_driver):
    loginPage = LoginPage(setup_driver)
    otpScreen = OtpScreen(setup_driver)

    loginPage.enter_phone_number()
    loginPage.click_on_login_as_streamer()
    loginPage.click_on_send_otp()
    otpScreen.enter_otp()
    otpScreen.click_on_verify()


# def test_register_as_streamer():
#     login_as_streamer(driver)
    
    # Need to handle the sign up process

def test_login_as_streamer(setup_driver):
    login_as_streamer(setup_driver)

# def test_streamer_flow(driver):
#     homePage = HomePage(driver)
#     login_as_streamer(driver)
    
#     gesture = GestureUtils(driver)
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
    
def test_go_live(setup_driver):
    # login_as_streamer(setup_driver)
    homePage = HomePage(setup_driver)
    homePage.go_online()
    homePage.go_live()