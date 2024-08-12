"""
Test_OrangeHRMPage.py
Program : Dat Driven  Framework main executable file
TestCase-01:
click the forgot password link and get a message "reset password link sent successfully"

"""

from Utilities.excel_functions import HRM_ExcelFunctions
from TestLocators.ForgotPasswordPage_locators import OrangeHRM_Forget_Password_Locators

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
#for Explicit Wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#TestCase-01
#forgot password link and see the message "reset password link sent" to yor mail
class OrangeHRM_Page:
    excel_file = OrangeHRM_Forget_Password_Locators().excel_file

    #for TestCase-01
    sheet_number_1 = OrangeHRM_Forget_Password_Locators().sheet_no_1
    #object creation for excel file
    forgot_password = HRM_ExcelFunctions(excel_file, sheet_number_1)

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    #To click the forget Password link
    def forgot_link_tc01(self):
        try:
            self.driver.get(OrangeHRM_Forget_Password_Locators().url)

            #row count from the Excel file
            row = self.forgot_password.row_count()

            for row in range(2, row + 1):
                username = self.forgot_password.read_data(row, 7)

                username_element = self.wait.until(
                    EC.presence_of_element_located((By.NAME, OrangeHRM_Forget_Password_Locators().username_locator)))
                #To validate the username textbox
                if username_element.is_displayed():
                    if username_element.is_enabled():
                        username_element.send_keys(username)

                        #forgot password link
                        forgot_password_element = self.wait.until(EC.element_to_be_clickable(
                            (By.XPATH, OrangeHRM_Forget_Password_Locators().forgot_password_locator)))
                        forgot_password_element.click()

                        return self.driver.current_url

        except NoSuchElementException as e:
            print(e)

    #To click the reset password link
    def reset_password(self):
        try:
            if OrangeHRM_Forget_Password_Locators().Reset_password_url == self.driver.current_url:

                reset_page_title = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, OrangeHRM_Forget_Password_Locators().reset_page_tittle))).text
                print("Reset Password Page Header :", reset_page_title)

                # row count from the Excel file
                row = self.forgot_password.row_count()

                for row in range(2, row + 1):
                    reset_username = self.forgot_password.read_data(row, 9)

                    reset_username_element = self.wait.until(EC.presence_of_element_located(
                        (By.NAME, OrangeHRM_Forget_Password_Locators().reset_username_locator)))
                    #To validate username element
                    if reset_username_element.is_displayed() and reset_username_element.is_enabled():
                        reset_username_element.send_keys(reset_username)

                        #To validate reset password element
                        reset_password_element = self.wait.until(EC.presence_of_element_located(
                            (By.XPATH, OrangeHRM_Forget_Password_Locators().reset_password_locator)))
                        if reset_password_element.is_displayed() and reset_password_element.is_enabled():
                            reset_password_element.click()

                    return self.driver.current_url
            else:
                print("Error : Reset password page is not loaded")

        except NoSuchElementException as e:
            print(e)

    #To see the Reset Password Link sent Page
    def link_page(self):
        try:
            if OrangeHRM_Forget_Password_Locators().success_page_url == self.driver.current_url:
                success_page_tittle = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, OrangeHRM_Forget_Password_Locators().success_locator))).text
                print("Reset Password Link sent Page Header :", success_page_tittle)

                return True

            else:
                print("Error: Reset password link sent page is not loaded")

        except NoSuchElementException as e:
            print(e)
        finally:
            self.driver.quit()
