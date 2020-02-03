*** Settings ***
Documentation   This file used to store all the URLs
Library         ../PythonScripts/csvLibrary.py
Library         ../venv/Lib/site-packages/site-packages/RequestsLibrary/
Library         RequestsLibrary
Library         Collections
Library         String
Library         ../PythonScripts/ArrayProcessor.py
Library         urllib3
Library          ../PythonScripts/RequestManager.py

*** Variables ***
${urls}
${responses}    []
${response}
${url}          https://bit.ly/2MMhOhs
${data}
*** Keywords ***
Initialize Array from CSV
    [Arguments]   ${csv_path}
    ${urls}=     read csv file    ${csv_path}
    set global variable           ${urls}
    ${urls}=      process array   ${urls}
    set global variable           ${urls}
    log                           ${urls}

Array verified
    [Arguments]     ${csv_path}
    verify_array    ${urls}  ${csv_path}

Send the request
    ${data}=    request hit
    log to console     ${data}
#    create session   my_session  ${url}     verify=True
#    ${response}=        GET REQUEST    my_session     ${url}    allow_redirects=${True}
#    log to console      ${response.status_code}
#    :FOR    ${url}  IN  @{urls}
#        \   LOG                 ${url}
#        \   ${response}=        get request    my_session     ${url}
#        \   log to console      ${response.status_code}
#        \   append to list      ${responses}    ${response}
#        \   LOG                 ${responses}
