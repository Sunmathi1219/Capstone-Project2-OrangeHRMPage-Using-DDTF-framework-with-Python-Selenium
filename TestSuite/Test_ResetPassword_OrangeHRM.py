""""
Main executable file for generating Html Report in Pytest for "Reset Password link message" TestCase-01
"""

from TestCases.ResetPasword_OrangeHRM import OrangeHRM_Page
from TestLocators.ForgotPasswordPage_locators import OrangeHRM_Forget_Password_Locators

import pytest

url = OrangeHRM_Forget_Password_Locators().url
OrangeHRM = OrangeHRM_Page(url)


#Test the forgot link is clickable and go the next page
def test_forgot_link_tc1():
    assert OrangeHRM.forgot_link_tc01() == OrangeHRM_Forget_Password_Locators().Reset_password_url
    print("SUCCESS : Reset password link is clicked successfully")


#Test the reset password link is cliable and go the next page
def test_reset_password():
    assert OrangeHRM.reset_password() == OrangeHRM_Forget_Password_Locators().success_page_url
    print("SUCCESS : Forget password link is clicked successfully")


#Test the Reset Password Link Sent page message is visible
def test_link_page():
    assert OrangeHRM.link_page() == True
    print("SUCCESS : Reset Password Link Sent Successfully textbox message is displayed successfully")
