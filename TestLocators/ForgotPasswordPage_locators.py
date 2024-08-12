""""
ForgotPasswordPage.py
Program : file containing locators for OrangeHRM Forgot password link
"""


#Testcase-01 - Orange HRM Forget Password Page Locating Elements and Relevant Data's'
class OrangeHRM_Forget_Password_Locators:
    #TestCase-01
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    Reset_password_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"

    username_locator = "username"
    forgot_password_locator = "//form[@class='oxd-form']//div[4]//p[text()='Forgot your password? ']"

    reset_page_tittle = "//*[@id='app']/div[1]/div[1]/div/form/h6[text()='Reset Password']"
    reset_username_locator = "username"
    reset_password_locator = "//button[@type='submit']"

    success_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"
    success_locator = "//*[@id='app']/div[1]/div[1]/div/h6[text()='Reset Password link sent successfully']"

    excel_file = "C:\\Users\\sunma\\PycharmProjects\\AT_Project_2\\TestData\\test_data_OrangeHRM.xlsx"
    sheet_no_1 = "Sheet1"
    pass_data = "Reset Password link sent successfully"

