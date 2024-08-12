""""
Admin_MenuOptions_Locators.py
Program : file containing locators for Admin Headers validation
"""


#TestCase-03 - OrangeHRM Admin page headers validation locators and data's
class OrangeHRM_Admin_Menu:
    #TestCase-03
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    username_locator = "username"
    password_locator = "password"
    submit_button = "//button[@type='submit']"

    excel_file = "C:\\Users\\sunma\\PycharmProjects\\AT_Project_2\\TestData\\test_data_OrangeHRM.xlsx"
    sheet_no = "Sheet1"

    admin_locator = "//a[@href='/web/index.php/admin/viewAdminModule']"
    pim_locator = "//a[@href='/web/index.php/pim/viewPimModule']"
    leave_locator = "//a[@href='/web/index.php/leave/viewLeaveModule']"


    time_module_locator = "//a[@href='/web/index.php/time/viewTimeModule']"
    recruitment_locator = "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']"
    my_info_locator = "//a[@href='/web/index.php/pim/viewMyDetails']"
    performance_module_locator = "//a[@href='/web/index.php/performance/viewPerformanceModule']"
    toast_locator = "//div[@id='oxd-toaster_1']//div//div//div[2]//p[text()='No Records Found']"
    toast_message = "No Records Found"

    dashboard_page_locator = "//a[@href='/web/index.php/dashboard/index']"
    directory_module_locator = "//a[@href='/web/index.php/directory/viewDirectory']"

    maintenance_page_locator = "//a[@href='/web/index.php/maintenance/viewMaintenanceModule']"
    maintenance_password_locator = "password"
    button_locator = "//button[@type='submit']"

    claim_page_locator = "//a[@href='/web/index.php/claim/viewClaimModule']"
    buzz_module_locator = "//a[@href='/web/index.php/buzz/viewBuzz']"


