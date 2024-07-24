*** Settings ***
Documentation        This is some basic info about the whole SUITE
Library              SeleniumLibrary


*** Variables ***



*** Test Cases ***
Verify user successfully open ruangguru link
    [Documentation]    Testcase for Login Cases
    [Tags]             TC1 Smoke Auth
    Log                Starting the test case ...
    Open Browser       https://www.ruangguru.com/    chrome
    Sleep              5s
    Close All Browsers

*** Keywords ***