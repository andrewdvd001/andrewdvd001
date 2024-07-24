*** Settings ***
Documentation        This is some basic info about the whole SUITE
Library              SeleniumLibrary

*** Variables ***

*** Test Cases ***
Verify user successfully opens Brain Academy link
    [Documentation]    Testcase for Login Cases
    [Tags]             TC1 Smoke Auth

    # Open Browser with maximized window
    Open Browser    https://app.brainacademy.id/    Chrome    options=add_argument("--start-maximized")

    # Selenium setup after opening browser
    Set Browser Implicit Wait    15s

    # Perform actions
    Click Link    Masuk/Daftar
    Input Text    name=emailOrPhone    andrew.david@ruangguru.com
    Click Button    Lanjutkan
    Input Text    name=password    adasubally
    Click Button    Masuk
    Page Should Contain    Bagian 1: Data Diri

    # Close browser
    Close All Browsers
