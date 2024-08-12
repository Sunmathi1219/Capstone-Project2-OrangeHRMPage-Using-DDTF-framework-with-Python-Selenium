
##  Tittle Of Project

OrangeHRM Web Page Automation- Project2

## Table of Contents:
       About OrangeHRM
       Overview of the Project
       Features
       Project Structure
       Tools and Technologies used
       Test Case Description
       

## About OrangeHRM
          OrangeHRM is an open-source Human Resource Management (HRM) system designed to streamline and automate HR processes for organizations. It provides a comprehensive suite of tools to manage various HR activities, including:
1.	Employee Information Management: Maintains a detailed database of employee information, including personal details, job titles, work experience, and more.
2.	Leave Management: Facilitates the tracking and management of employee leave requests, approvals, and balances.
3.	Time and Attendance Management: Monitors employee work hours, attendance, and schedules.
4.	Performance Management: Supports performance evaluations, goal setting, and appraisals.
5.	Recruitment and Onboarding: Manages the recruitment process, from job postings to candidate tracking and onboarding.
6.	Employee Self-Service: Allows employees to access and update their personal information, submit leave requests, and view their attendance records.
7.	Reporting and Analytics: Provides various reports and analytics to help HR managers make informed decisions.
OrangeHRM is highly customizable and can be extended with additional modules to meet the specific needs of an organization. It is available in both free and paid versions, with the paid versions offering more advanced features and support.
 you can automate various tests and interactions with the OrangeHRM system, such as verifying login functionality, managing employee records, and ensuring the correct functioning of different modules.

## Overview of the Project
        This project is an automated testing suite for the OrangeHRM open-source Human Resource Management system. It utilizes Selenium WebDriver with Python in a data-driven framework to ensure comprehensive test coverage and robustness. The primary goal is to automate the functional and regression testing of the OrangeHRM system.
          This project focuses on automating test cases for the OrangeHRM web application using Selenium with Python. The automation framework is built using a Data-Driven Testing Framework (DDTF) approach, which allows for easy management and execution of test cases with varying inputs. Additionally, the project generates an HTML report after the execution of test cases to summarize the results.

## Features:
      Automated testing for OrangeHRM web application.
Data-driven testing framework using Selenium with Python.
Detailed pytest HTML reports.

## Project Structure
        The project is structured to be modular and scalable, making it easy to add or modify test cases. The key components include:
•	Test Cases: A set of automated test cases covering the core functionalities of the OrangeHRM application.
•	Data Files: External data files (e.g., CSV, Excel) are used to drive the inputs for the test cases.
•	Selenium WebDriver: Used for interacting with the web elements on the OrangeHRM application.
•	Pytest: The testing framework used to execute the test cases.
•	HTML Report: A detailed report generated after the execution of the test cases, providing a summary of the results.

## Tools and Technologies Used:
      •	Selenium WebDriver: For automating browser interactions.
      • Python: The programming language used for writing the test scripts.
      •	Pytest: The testing framework used for running the test cases.
      •	Data-Driven Testing Framework (DDTF): Utilized to separate the test data from the test scripts, making the tests more flexible and easier to maintain.
      •	Data Management: openpyxl (for Excel-based data-driven testing)
      •	HTML Report: Generated using pytest-html or a similar plugin to provide a visual summary of the test execution results.
      •	PyCharm: The integrated development environment (IDE) used for coding and managing the project.

## TestCases Description:
This project contains the following three test cases:
## TestCase-01:
## Test Objective:
          Forgot password link validation on OrangeHRM login page
          URL = “https://opensource-demo.orangehrmlive.com/web/index.php/auth/login”
## Preconditions:
1.	Launch the URL
2.	Orange HRM is launched on a compatible browser
3.	Click on “forgot password” link
## Steps:
1.	Username textbox is available
2.	Provide username 
3.	Click on Reset Password 
## Expected condition:
              The user should be able to see the username box and get a successful message saying “Reset Password Link Sent Successfully”


## Test Case – 02:
## Test Objective:
            Header validation on Admin Page
## Precondition:
1.	Launch the URL
2.	Orange HRM site is launched on a compatible browser

## Steps:
               1.Go to the Admin page and Validate “Tittle” of the page as “Orange HRM”
               2.Validate the below options are displaying on Admin page 
•	User Management
•	Job
•	Organization
•	Qualifications
•	Nationalities
•	Corporate Banking
•	Configuration

## Expected Result:
            The user should be able to see the above mentioned Admin page Headers on Admin page

## Test Case -03:
## Test Objective:
             Main Menu Validation on Admin page
## Precondition:
            Launch URL and login as “Admin”
            Orange HRM site is launched on a compatible browser
## Steps:
           1. Go to Admin page
           2. Validate the below Options are displaying on Admin page
•	Admin
•	PIM
•	Leave
•	Time
•	Recruitment
•	My Info
•	Performance
•	Dashboard
•	Directory
•	Maintenance
•	Buzz
## Expected Result:
           The User should be able to see the above mentioned Admin page Menu items on Admin page


Expected Result:
           The User should be able to see the above mentioned Admin page Menu items on Admin page
