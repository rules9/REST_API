*** Settings ***
Documentation   This file used to store all the URLs
Library         ../venv/Lib/site-packages/site-packages/RequestsLibrary/
Library         RequestsLibrary
Library         Collections
Library         ../PythonScripts/arrayProcessor.py
Library         ../PythonScripts/csvLibrary.py

*** Variables ***
${urls}
${reshape_urls}
${total_urls}
${number_arrays}

*** Keywords ***
Initialize URL Array from CSV
    [Arguments]   ${csv_path}
    ${urls}=     read csv file    ${csv_path}
    set global variable           ${urls}
    ${urls}=      flat array      ${urls}
    set global variable           ${urls}

URL Array verified
    [Arguments]     ${csv_path}
    verify_array    ${urls}  ${csv_path}

Create Multiple URL Arrays Instance
    [Arguments]     ${batch_size}
    ${reshape_urls}     ${total_urls}   ${number_arrays}=     reshape array     ${urls}     ${batch_size}
    set global variable      ${reshape_urls}
    set global variable      ${total_urls}
    set global variable      ${number_arrays}

Verify the Numbser of URL Arrays created
#    log to console          ${reshape_urls}
    log to console          ${total_urls}
    log to console          ${number_arrays}

