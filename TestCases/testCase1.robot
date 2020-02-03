*** Settings ***
Documentation       This file will cover the user story
Resource            ../TestKeywords/Create_URLs.robot

*** Variables ***
${csv_path}     TestData/URLs.csv

*** Test Cases ***
1. Array of all the URLs given in csv should get created and verifed
    Initialize Array from CSV   ${csv_path}
    Array verified      ${csv_path}

2. Send the request to the server
    Send the request
