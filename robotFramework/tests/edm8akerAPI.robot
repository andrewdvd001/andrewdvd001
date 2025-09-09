*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary

*** Variables ***
${BASE_URL}    https://example.com
${ENDPOINT}    /api/activities?sort=newest

*** Test Cases ***
Validate API Status And Response Body
    [Documentation]    Sends a GET request, validates status code, and checks that 'createdAt' exists in each row
    Create Session    api    ${BASE_URL}
    ${response}=    GET On Session    api    ${ENDPOINT}
    Status Should Be    200    ${response}

    ${json}=    To Json    ${response.content}
    Dictionary Should Contain Key    ${json}    data
    Dictionary Should Contain Key    ${json["data"]}    rows

    ${rows}=    Get From Dictionary    ${json["data"]}    rows
    Should Not Be Empty    ${rows}

    FOR    ${row}    IN    @{rows}
        Dictionary Should Contain Key    ${row}    createdAt
        ${created_at}=    Get From Dictionary    ${row}    createdAt
        Should Match Regexp    ${created_at}    ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$
    END
