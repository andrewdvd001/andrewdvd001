*** Settings ***
Library    SeleniumLibrary

Suite Setup       Open Maker Cart Studio
Suite Teardown    Close Browser

*** Variables ***
${BROWSER}                  chrome
${BASE_URL}                 https://builder.eddy4teachers.com/makercart-studio
${LOC_GRADE_FILTER}         xpath=//input[@placeholder='Grade']
${LOC_CHECKBOX_1}           xpath=//input[@id='checkbox-1']
${LOC_CHECKBOX_2}           xpath=//input[@id='checkbox-2']
${LOC_ITEM_GRID}            xpath=//div[@class='item-grid-container']
${LOC_FIRST_ACTIVITY}       xpath=(//div[contains(@class,'item-maker-cart')])[1]
${LOC_SUBJECT_CONTAINER}    xpath=//div[@class='subject-container']
@{EXPECTED_AGE_GROUPS}      Lower Elementary    Upper Elementary

*** Keywords ***
Open Maker Cart Studio
    Open Browser    about:blank    ${BROWSER}
    Maximize Browser Window
    Go To    ${BASE_URL}
    Wait Until Page Contains Element    ${LOC_ITEM_GRID}

Apply Age Group Filter
    [Arguments]    ${filter_locator}
    Click Element    ${LOC_GRADE_FILTER}    
    Click Element    ${filter_locator}
    Click Element    ${LOC_GRADE_FILTER}
    Wait Until Element Is Visible   ${LOC_FIRST_ACTIVITY}    5s

Open First Activity
    Click Element    ${LOC_FIRST_ACTIVITY}
    Wait Until Element Is Visible    ${LOC_SUBJECT_CONTAINER}    5s    

Element Should Contain Any
    [Arguments]    ${locator}    @{expected_texts}
    ${text}=    Get Text    ${locator}
    ${found}=    Set Variable    False
    FOR    ${value}    IN    @{expected_texts}
        IF    '${value}' in '${text}'
            ${found}=    Set Variable    True
            Exit For Loop
        END
    END
    Should Be True    ${found}    Expected one of ${expected_texts} in element ${locator}, but got: ${text}


*** Test Cases ***
TC-002 Verify filter by multiple Age Groups
    [Documentation]    Ensure applying multiple Age Group filters updates the results list correctly.
    [Tags]    Smoke    Functional
    Apply Age Group Filter    ${LOC_CHECKBOX_1}
    Apply Age Group Filter    ${LOC_CHECKBOX_2}
    Open First Activity
    Element Should Contain Any    ${LOC_SUBJECT_CONTAINER}    @{EXPECTED_AGE_GROUPS}

