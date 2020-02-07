*** Settings ***
Documentation       This file will cover the user story of verifying GET request with Object Count and Null occurance
Resource            ../TestKeywords/generate_URLs.robot
Resource            ../TestKeywords/request_manager.robot

*** Variables ***
${csv_path}     TestData/URLs.csv
${batch_size}   5

*** Test Cases ***
1. Array of all the URLs given in csv should get created and verifed
    Initialize URL Array from CSV   ${csv_path}
    verified URL Array              ${csv_path}

2. Array URL distribution and corresponding Request-hit should get completed successfully
    Create Multiple URL Arrays Instance         ${batch_size}
    Verify the Numbser of URL Arrays created
    Sending Requests to the server
    Verify the Response with Error(if any)