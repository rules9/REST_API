*** Settings ***
Documentation   This file used to store all the URLs
Library         ../PythonScripts/csvLibrary.py

*** Variables ***
${urls}

*** Keywords ***
Initialize Array from CSV
    ${urls}=      read csv file  TestData/URLs.csv
Verify the array
    log     ${urls}
