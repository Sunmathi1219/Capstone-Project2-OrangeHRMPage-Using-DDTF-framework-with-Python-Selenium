""""
Main executable file for generating Html Report in Pytest for validating the menu options on Admin Page- TestCase-02
To Test the OrangeHRM Admin page tittle and Header validations
"""

from TestCases.Admin_Headers import AdminPageHeaders
from TestLocators.Adminpage_Header_Locators import OrangeHRM_Admin_Header

import pytest

url = OrangeHRM_Admin_Header().url
admin_headers = AdminPageHeaders(url)


#To test the OrangeHRM Login Page validation
def test_OrangeHRM_Login():
    assert admin_headers.OrangeHRM_Login() == OrangeHRM_Admin_Header.dashboard_url
    print("SUCCESS : Successfully login into the dashboard")


#To test the OrangeHRM admin page tittle validation
def test_AdminPage_Tittle():
    assert admin_headers.AdminPage_Tittle() == True
    print("SUCCESS : Admin Page Tittle is validated Successfully")


#To test the OrangeHRM user management Page validation
def test_UserManagement():
    assert admin_headers.UserManagement() == OrangeHRM_Admin_Header.User_management_text
    print("SUCCESS : User Management Header is validated Successfully with text : {a}".format(
        a=OrangeHRM_Admin_Header.User_management_text))


#To test the OrangeHRM admin page job header validation
def test_Job():
    assert admin_headers.Job() == OrangeHRM_Admin_Header.job_text
    print("SUCCESS : Job Header is validated Successfully with text : {a}".format(
        a=OrangeHRM_Admin_Header.job_text))


#To test the OrangeHRM admin page organization header validation
def test_Organization():
    assert admin_headers.Organization() == OrangeHRM_Admin_Header.organization_text
    print("SUCCESS : Organization Header is validated Successfully with text : {a}".format(
        a=OrangeHRM_Admin_Header.organization_text))


#To test the OrangeHRM admin page qualification header validation
def test_Qualification():
    assert admin_headers.Qualification() == OrangeHRM_Admin_Header.qualification_text
    print("SUCCESS : Qualification Header is validated Successfully with text : {a}".format(
        a=OrangeHRM_Admin_Header.qualification_text))


#To test the OrangeHRM admin page nationalities header validation
def test_Nationalities():
    assert admin_headers.Nationalities() == True
    print("SUCCESS : Nationalities Header is validated Successfully")


#To test the OrangeHRM admin page Corporate_Branding header validation
def test_Corporate_Branding():
    assert admin_headers.Corporate_Branding() == True
    print("SUCCESS : Corporate_Branding Header is validated Successfully")


#To test the OrangeHRM admin page Configuration header validation
def test_Configuration():
    assert admin_headers.Configuration() == OrangeHRM_Admin_Header.configuration_text
    print("SUCCESS : Configuration Header is validated Successfully with text : {a}".format(
        a=OrangeHRM_Admin_Header.configuration_text))
