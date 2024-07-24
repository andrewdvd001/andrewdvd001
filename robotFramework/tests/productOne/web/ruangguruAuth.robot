*** Settings ***
Documentation    This is some basic info about the whole SUITE
Resource    ../../../resources/common.resource
Resource    ../../../resources/productOne/web/brainacademy.resource

*** Variables ***

*** Test Cases ***
Verify user successfully Login in Brain Academy with valid credential
    [Documentation]    Testcase for Login Cases
    [Tags]             TC1 Smoke Auth

    common.Begin Web Test
    brainacademy.Access brainacademy
    brainacademy.Open login page
    brainacademy.Fill correct email
    brainacademy.Fill correct password
    common.Close browser
    
Verify user failed to Login in Brain Academy with invalid password
    [Documentation]    Testcase for Login failed Cases
    [Tags]             TC2 Smoke Auth

    common.Begin Web Test
    brainacademy.Access brainacademy
    brainacademy.Open login page
    brainacademy.Fill correct email
    common.Close browser
    