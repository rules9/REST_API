*** Settings ***
Documentation       This file will have the keywords for the Get Request hitting the server and storing response
Library             ../venv/Lib/site-packages/site-packages/RequestsLibrary/
Library             RequestsLibrary
Library             Collections
Library             ../PythonScripts/multiprocess_requestManager.py
Resource            generate_URLs.robot
Library             thread

*** Variables ***
${response}


*** Keywords ***
Sending Requests to the server
    ${response}=    request process         ${reshape_urls}
    log to console      ${response}
    log                 ${response}



