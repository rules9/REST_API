*** Settings ***
Documentation       This file will have the keywords for the Get Request hitting the server and storing the response
Library             ../PythonScripts/requestManager.py
Resource            generate_URLs.robot

*** Variables ***
${response_segment}

*** Keywords ***
Sending Requests to the server

    ${response_segment}=     process requests      ${reshape_urls}
    log                     ${response_segment}

Verify the Response with Error(if any)




