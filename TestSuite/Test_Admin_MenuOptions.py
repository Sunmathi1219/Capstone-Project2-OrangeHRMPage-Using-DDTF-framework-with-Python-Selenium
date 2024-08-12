""""
Main executable file for generating Html Report in Pytest for validating the menu options on Admin Page- TestCase-03
"""

from TestCases.Admin_MenuOptions import AdminPageMenu
from TestLocators.Admin_MenuOptions_Locators import OrangeHRM_Admin_Menu

import pytest

url = OrangeHRM_Admin_Menu().url
admin_menu = AdminPageMenu(url)


#To test the OrangeHRM Login Page validation
def test_OrangeHRM_Login():
    assert admin_menu.OrangeHRM_Login() == OrangeHRM_Admin_Menu().dashboard_url
    print("SUCCESS: user login into the dashboard url successfully")


# To test the OrangeHRM Admin Page validation
def test_AdminPage():
    assert admin_menu.AdminPage() == True
    print("SUCCESS : Admin Page is validated Successfully")


#To test the OrangeHRM PIM Page validation
def test_PIMPage():
    assert admin_menu.PIMPage() == True
    print("Success : PIM Page is validated Successfully")


#To test the OrangeHRM Leave Page validation
def test_LeavePage():
    assert admin_menu.LeavePage() == True
    print("SUCCESS: Leave Page is validated successfully")


#To test the OrangeHRM Time Page validation
def test_TimeModule():
    assert admin_menu.TimeModule() == True
    print("Success : Time Module is validated Successfully ")


#To test the OrangeHRM Recruitment Page validation
def test_RecruitmentPage():
    assert admin_menu.RecruitmentPage() == True
    print("SUCCESS : Recruitment page is validated Successfully")


#To test the OrangeHRM MyInfo Page validation
def test_MyInfoPage():
    assert admin_menu.MyInfoPage() == True
    print("SUCCESS : MyInfo Page is validated Successfully")


#To test the OrangeHRM Performance Page validation
def test_Performance_Module():
    assert admin_menu.Performance_Module() == OrangeHRM_Admin_Menu().toast_message
    print(
        "SUCCESS : Performance Page is validated Successfully and Toast Message is displayed : {Toast_Message}".format(
            Toast_Message=admin_menu.Performance_Module()))


#To test the OrangeHRM Dashboard Page validation
def test_DashboardPage():
    assert admin_menu.DashboardPage() == True
    print("SUCCESS : Dashboard Page is validated Successfully")


#To test the OrangeHRM Directory Page validation
def test_DirectoryModule():
    assert admin_menu.DirectoryModule() == True
    print("SUCCESS : Directory Module is validated Successfully")


#To test the OrangeHRM Maintenance Page validation
def test_MaintenancePage():
    assert admin_menu.MaintenancePage() == True
    print("SUCCESS : Maintenance Page is validated Successfully")


#To test the OrangeHRM Claim Page validation
def test_ClaimPage():
    assert admin_menu.ClaimPage() == True
    print("SUCCESS : Claim Page is validated Successfully")


#To test the OrangeHRM Buzz Page validation
def test_BuzzModule():
    assert admin_menu.BuzzModule() == True
    print("SUCCESS : Buzz Page is validated Successfully")
