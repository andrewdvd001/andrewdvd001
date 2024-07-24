*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Begin Web Test
    Open Browser    about:blank    Chrome    options=add_argument("--start-maximized")
    Set Selenium Speed    1s
    Set Selenium Timeout    10s

Close browser
    Close All Browsers