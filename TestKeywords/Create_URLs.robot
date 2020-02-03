*** Settings ***
Documentation   This file used to store all the URLs
Library         ../PythonScripts/csvLibrary.py
Library         ../venv/Lib/site-packages/site-packages/RequestsLibrary/
Library         RequestsLibrary
Library         Collections
Library         String
Library         ../PythonScripts/ArrayProcessor.py

*** Variables ***
${urls}
${my_session}
${responses}
${response}
${url}
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
    :FOR    ${url}  IN  @{urls}
        \   create session      ${my_session}   ${url}
        \   LOG                 ${url}
        \   ${response}=        get request     ${my_session}   ${url}
        \   lOG                 ${response}
        \   append to list      ${responses}    ${response}
        \   LOG                 ${responses}
