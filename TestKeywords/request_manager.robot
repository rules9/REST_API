*** Settings ***
Documentation       This file will have the keywords for the Get Request hitting the server and storing response
Library             Collections
#Library             ../PythonScripts/multiprocess_requestManager.py
Library             ../PythonScripts/responseManager.py
Resource            generate_URLs.robot

*** Variables ***
${request_segment}
${response1}
${response2}
${response3}
${segment_counter1}      0
${segment_counter2}      1
${segment_counter3}      2
${segment_counter4}      3

*** Keywords ***
Sending Requests to the server
    ${request_segment}=     request pre processing      ${reshape_urls}
    log to console          ${request_segment}
    log                     ${request_segment}





