*** Settings ***
Documentation   This file used to store all the URLs and making it ready for get processed
Library         Collections
Library         ../PythonScripts/arrayProcessor.py
Library         ../PythonScripts/csvLibrary.py

*** Variables ***
${urls}
${reshape_urls}
${total_urls}
${number_arrays}
${size_of_array}

*** Keywords ***

Initialize URL Array from CSV
    [Arguments]   ${csv_path}
    ${urls}=     read csv file    ${csv_path}
    ${urls}=      flat array      ${urls}
    set global variable           ${urls}


verified URL Array
    [Arguments]     ${csv_path}
    verify_array    ${urls}         ${csv_path}


Create Multiple URL Arrays Instance
    [Arguments]     ${batch_size}
    ${reshape_urls}     ${total_urls}   ${number_arrays}    ${size_of_array}=     reshape array     ${urls}     ${batch_size}

    set global variable      ${reshape_urls}
    set global variable      ${total_urls}
    set global variable      ${number_arrays}
    set global variable      ${size_of_array}


Verify the Numbser of URL Arrays created
    log    ${reshape_urls}
    log    ${total_urls}
    log    ${number_arrays}
    log    ${size_of_array}
