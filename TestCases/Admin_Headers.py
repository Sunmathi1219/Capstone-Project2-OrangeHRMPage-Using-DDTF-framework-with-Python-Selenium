"""
Admin_Headers.py
Program : Dat Driven  Framework main executable file
TestCase-02:
Validate the Admin Module Tittle and  Headers of Admin Page on OrangeHRM
"""

from Utilities.excel_functions import HRM_ExcelFunctions
from TestLocators.Adminpage_Header_Locators import OrangeHRM_Admin_Header

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
#for Explicit Wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#Te-02 -AdminPage Header validation
class AdminPageHeaders:
    excel_file = OrangeHRM_Admin_Header().excel_file

    #for TestCase-02
    sheet_number = OrangeHRM_Admin_Header().sheet_no

    admin_header_tc2 = HRM_ExcelFunctions(excel_file, sheet_number)

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    #TestCase-02-Admin Page Header Validation
    #OrangeHRM Page Login with valid input and output
    def OrangeHRM_Login(self):
        try:
            self.driver.get(OrangeHRM_Admin_Header().url)

            # row count from the Excel file
            row = self.admin_header_tc2.row_count()

            for row in range(2, row + 1):
                username = self.admin_header_tc2.read_data(row, 7)
                password = self.admin_header_tc2.read_data(row, 8)

                user_name = self.wait.until(
                    EC.presence_of_element_located((By.NAME, OrangeHRM_Admin_Header().username_locator)))
                user_name.send_keys(username)

                pass_word = self.wait.until(
                    EC.presence_of_element_located((By.NAME, OrangeHRM_Admin_Header().password_locator)))
                pass_word.send_keys(password)

                login_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Header().submit_button)))
                login_button.click()
                print("Successfully login into the dashboard with username {a} and password {b}".format(a=username,
                                                                                                        b=password))
                return self.driver.current_url
            else:
                return False

        except NoSuchElementException as e:
            print(e)

    #Admin page Tittle validation
    def AdminPage_Tittle(self):
        try:
            if OrangeHRM_Admin_Header().dashboard_url == self.driver.current_url:

                admin_element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Header().admin_locator)))

                # check the visibility of Admin Tittle
                if admin_element.is_displayed():
                    if admin_element.is_enabled():
                        admin_element.click()
                        print("Admin Page Tittle:", self.driver.title)
                        return True
                else:
                    return False

        except NoSuchElementException as e:
            print(e)

    #User Management header validation in Admin Page
    def UserManagement(self):
        try:
            user_management_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Header().user_management_locator)))

            #check the visibility of user management header
            if user_management_element.is_displayed():
                if user_management_element.is_enabled():
                    user_management_element.click()

                    return user_management_element.text

            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Job header validation in Admin Page
    def Job(self):
        try:
            job_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Header().job_locator)))

            # check the visibility of job header
            if job_element.is_displayed():
                if job_element.is_enabled():
                    job_element.click()
                    return job_element.text

            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Organization header validation in Admin Page
    def Organization(self):
        try:
            organization_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Header().organization_locator)))

            # check the visibility of organization header
            if organization_element.is_displayed():
                if organization_element.is_enabled():
                    organization_element.click()

                    return organization_element.text

            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Qualification header validation in Admin Page
    def Qualification(self):
        try:

            qualification_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Header().qualification_locator)))

            # check the visibility of qualification header
            if qualification_element.is_displayed():
                if qualification_element.is_enabled():
                    self.driver.execute_script("arguments[0].click();", qualification_element)
                    return qualification_element.text

            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Nationalities header validation in Admin Page
    def Nationalities(self):
        try:

            nationality_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Header().nationality_locator)))

            # check the visibility of Nationalities header
            if nationality_element.is_displayed():
                if nationality_element.is_enabled():
                    self.driver.execute_script("arguments[0].click();", nationality_element)

                    return True

            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Nationalities header validation in Admin Page
    def Corporate_Branding(self):
        try:

            corporate_branding_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Header().corporate_branding_locator)))

            # check the visibility of corporate-branding header
            if corporate_branding_element.is_displayed():
                if corporate_branding_element.is_enabled():
                    self.driver.execute_script("arguments[0].click();", corporate_branding_element)
                    return True

            else:
                return False

        except NoSuchElementException as e:
            print(e)

    # Configuration header validation in Admin Page
    def Configuration(self):
        try:
            configuration_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, OrangeHRM_Admin_Header().configuration_locator)))

            # check the visibility of configuration header
            if configuration_element.is_displayed():
                if configuration_element.is_enabled():
                    self.driver.execute_script("arguments[0].click();", configuration_element)

                    return configuration_element.text

            else:
                return False

        except NoSuchElementException as e:
            print(e)

        finally:
            self.driver.quit()
