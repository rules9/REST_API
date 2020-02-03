*** Settings ***
Documentation   This file used to store all the URLs
Library         ../PythonScripts/csvLibrary.py

*** Variables ***
${urls}

*** Keywords ***
Initialize Array from CSV
    [Arguments]   ${csv_path}
    ${urls}=      read csv file     ${csv_path}
    log     ${urls}
Array verified
    [Arguments]     ${csv_path}
    verify_array    ${urls}  ${csv_path}

