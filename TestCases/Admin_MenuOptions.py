"""
Admin_MenoOptions.py
Program : Dat Driven  Framework main executable file
TestCase-03:
Validate the Menu options are displayed on the Admin Page
"""

from Utilities.excel_functions import HRM_ExcelFunctions
from TestLocators.Admin_MenuOptions_Locators import OrangeHRM_Admin_Menu

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
#for Explicit Wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#TC-03 -  AdminPage Menu validation
class AdminPageMenu:
    excel_file = OrangeHRM_Admin_Menu().excel_file

    #for TestCase-03
    sheet_number = OrangeHRM_Admin_Menu().sheet_no

    admin_header_tc2 = HRM_ExcelFunctions(excel_file, sheet_number)

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    #TestCase-03-Admin Page Menu Validation
    #OrangeHRM Page Login with valid input and output
    def OrangeHRM_Login(self):
        try:
            self.driver.get(OrangeHRM_Admin_Menu().url)

            # row count from the Excel file
            row = self.admin_header_tc2.row_count()

            for row in range(2, row + 1):
                username = self.admin_header_tc2.read_data(row, 7)
                password = self.admin_header_tc2.read_data(row, 8)

                user_name = self.wait.until(
                    EC.presence_of_element_located((By.NAME, OrangeHRM_Admin_Menu().username_locator)))
                user_name.send_keys(username)

                pass_word = self.wait.until(
                    EC.presence_of_element_located((By.NAME, OrangeHRM_Admin_Menu().password_locator)))
                pass_word.send_keys(password)

                login_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().submit_button)))
                login_button.click()

                return self.driver.current_url
            else:
                return False

        except NoSuchElementException as e:
            print(e)

    #Admin page  validation
    def AdminPage(self):
        try:
            if OrangeHRM_Admin_Menu().dashboard_url == self.driver.current_url:

                admin_element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().admin_locator)))

                # check the visibility of Admin Page validation
                if admin_element.is_displayed():
                    if admin_element.is_enabled():
                        admin_element.click()
                        return True
                else:
                    return False

        except NoSuchElementException as e:
            print(e)

    # PIM page validation
    def PIMPage(self):
        try:
            pim_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().pim_locator)))

            # check the visibility of PIM Page validation
            if pim_element.is_displayed():
                if pim_element.is_enabled():
                    pim_element.click()
                    return True
            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Leave page validation
    def LeavePage(self):
        try:
            leave_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().leave_locator)))

            # check the visibility of leave page validation
            if leave_element.is_displayed():
                if leave_element.is_enabled():
                    leave_element.click()
                    return True

            else:
                print("ERROR")
                return False

        except NoSuchElementException as e:
            print(e)

    # Time Module validation
    def TimeModule(self):
        try:

            time_module_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().time_module_locator)))

            # check the visibility of Time Page validation
            if time_module_element.is_displayed():
                if time_module_element.is_enabled():
                    time_module_element.click()

                    return True
            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Recruitment Module validation
    def RecruitmentPage(self):
        try:
            recruitment_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().recruitment_locator)))

            # check the visibility of Recruitment Module Validation
            if recruitment_element.is_displayed():
                if recruitment_element.is_enabled():
                    recruitment_element.click()
                    return True
            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # MyInfo Module validation
    def MyInfoPage(self):
        try:
            my_info_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().my_info_locator)))

            # check the visibility of MyInfo Module validation
            if my_info_element.is_displayed():
                if my_info_element.is_enabled():
                    my_info_element.click()
                    return True
            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Performance Module validation
    def Performance_Module(self):
        try:
            performance_module_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().performance_module_locator)))

            # check the visibility of performance page validation
            if performance_module_element.is_displayed():
                if performance_module_element.is_enabled():
                    performance_module_element.click()

                    # toast message for No Record Found text message validation
                    toast_message_element = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().toast_locator)))
                    if toast_message_element.is_displayed():
                        if toast_message_element.is_enabled():
                            text_message1 = self.wait.until(
                                EC.element_to_be_clickable(
                                    (By.XPATH, OrangeHRM_Admin_Menu().toast_locator))).text
                            print("Toast Message For Performance module page validation is displayed: ", text_message1)
                            return text_message1
                    else:
                        print("ERROR : Toast Message Not Found")
                        return False

        except NoSuchElementException as e:
            print(e)

    # Dashboard Page validation
    def DashboardPage(self):
        try:
            dashboard_page_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().dashboard_page_locator)))

            # check the visibility of DashBoard Page validation
            if dashboard_page_element.is_displayed():
                if dashboard_page_element.is_enabled():
                    dashboard_page_element.click()
                    return True
            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Directory Module Page validation
    def DirectoryModule(self):
        try:
            directory_module_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().directory_module_locator)))

            # check the visibility of Directory Module validation
            if directory_module_element.is_displayed():
                if directory_module_element.is_enabled():
                    directory_module_element.click()
                    return True
            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Maintenance Page validation
    def MaintenancePage(self):

        try:
            maintenance_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().maintenance_page_locator)))

            # check the visibility of Maintenance page validation
            if maintenance_element.is_displayed():
                if maintenance_element.is_enabled():
                    maintenance_element.click()

                    # row count from the Excel file
                    row = self.admin_header_tc2.row_count()

                    for row in range(2, row + 1):
                        password1 = self.admin_header_tc2.read_data(row, 8)

                        password_element = self.wait.until(EC.presence_of_element_located(
                            (By.NAME, OrangeHRM_Admin_Menu().maintenance_password_locator)))
                        if password_element.is_displayed() and password_element.is_enabled():
                            password_element.send_keys(password1)

                            confirm_button = self.wait.until(
                                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu.button_locator)))
                            if confirm_button.is_displayed() and confirm_button.is_enabled():
                                confirm_button.click()

                                return True
            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Claim Page validation
    def ClaimPage(self):
        try:
            claim_page_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().claim_page_locator)))

            # check the visibility of claim page validation
            if claim_page_element.is_displayed():
                if claim_page_element.is_enabled():
                    claim_page_element.click()

                    return True
            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Buzz module validation
    def BuzzModule(self):
        try:
            buzz_module_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Menu().buzz_module_locator)))

            # check the visibility of Buzz module validation
            if buzz_module_element.is_displayed():
                if buzz_module_element.is_enabled():
                    buzz_module_element.click()

                    return True
            else:
                return False

        except NoSuchElementException as e:
            print(e)

        finally:
            self.driver.quit()
