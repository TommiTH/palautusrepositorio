*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalleboy
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kalleeeeeee
    Set Password Confirmation  kalleeeeeee
    Submit Credentials
    Register Should Fail With Message  Password has to include at least 1 non a - z character

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle122
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Password confirmation doesn't match password

Login After Successful Registration
    Set Username  uloskirjautuja
    Set Password  pekkak1234
    Set Password Confirmation  pekkak1234
    Submit Credentials
    Logout
    Go To Login Page
    Set Username  uloskirjautuja
    Set Password  pekkak1234
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  epaonnistuvakirjautuja
    Set Password  12345
    Set Password Confirmation  54321
    Submit Credentials
    Logout
    Go To Login Page
    Set Username  epaonnistuvakirjautuja
    Set Password  12345
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
