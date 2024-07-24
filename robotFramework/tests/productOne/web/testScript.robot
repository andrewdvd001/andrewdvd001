*** Settings ***
Documentation        This is some basic info about the whole SUITE
Library              SeleniumLibrary

*** Variables ***

*** Test Cases ***
Verify user successfully Login in Brain Academy with valid credential
    [Documentation]    Testcase for Login Cases
    [Tags]             TC1 Smoke Auth

    Begin Web Test
    Access brainacademy
    Open login page
    Fill correct email
    Fill correct password
    Close browser
    
Verify user failed to Login in Brain Academy with invalid password
    [Documentation]    Testcase for Login failed Cases
    [Tags]             TC2 Smoke Auth

    Begin Web Test
    Access brainacademy
    Open login page
    Fill correct email
    Close browser
    
*** Keywords ***
Begin Web Test
    Open Browser    about:blank    Chrome    options=add_argument("--start-maximized")
    Set Browser Implicit Wait    3s

Access brainacademy
    Go To    https://app.brainacademy.id
    Page Should Contain    Brain Academy Online

Open login page
    Click Link    Masuk/Daftar
    Page Should Contain    Yuk, daftar atau masuk sekarang.

Fill correct email
    Input Text    name=emailOrPhone    andrew.david@ruangguru.com
    Click Button    Lanjutkan
    Page Should Contain    Halo! Selamat datang kembali!
    
Fill correct password
    Input Text    name=password    adasubally
    Click Button    Masuk
    Page Should Contain    Andrew D

Fill incorrect password
    Input Text    name=password    adasubally1
    Click Button    Masuk
    Page Should Contain    Email atau password yang dimasukkan salah.


Close browser
    Close All Browsers