""""
Admin_Header.py
Program : file containing locators for Admin Headers and Admin Tittle
"""


#TestCase-02 - Admin page Tittle and Header validation locators and data's
class OrangeHRM_Admin_Header:
    #TestCase-02
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    username_locator = "username"
    password_locator = "password"
    submit_button = "//button[@type='submit']"

    admin_page_tittle = "//img[@src='/web/images/orangehrm-logo.png?v=1721393199309']"
    admin_locator = "//a[@href='/web/index.php/admin/viewAdminModule']"

    excel_file = "C:\\Users\\sunma\\PycharmProjects\\AT_Project_2\\TestData\\test_data_OrangeHRM.xlsx"
    sheet_no = "Sheet1"

    user_management_locator = "//div[@class='oxd-topbar-body']//nav//li[1]//span"
    job_locator = "//div[@class='oxd-topbar-body']//nav//li//span[text()='Job ']"
    organization_locator = "//div[@class='oxd-topbar-body']//nav//li//span[text()='Organization ']"
    qualification_locator = "//div[@class='oxd-topbar-body']//nav//li[4]//span[text()='Qualifications ']"
    nationality_locator = "//div[@class='oxd-topbar-body']//nav//li[5]//a"
    corporate_branding_locator = "//div[@class='oxd-topbar-body']//nav//li[6]//a[text()='Corporate Branding']"
    configuration_locator = "//div[@class='oxd-topbar-body']//nav//li[7]//span[text()='Configuration ']"

    User_management_text = "User Management"
    job_text = "Job"
    organization_text = "Organization"
    qualification_text = "Qualifications"
    configuration_text = "Configuration"

