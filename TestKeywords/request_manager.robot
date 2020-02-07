*** Settings ***
Documentation       This file will have the keywords for the Get Request hitting the server and storing the response
Library             ../PythonScripts/requestManager.py
Resource            generate_URLs.robot

*** Variables ***
${response_objects}
${total_null_values}
${errors_&_count}

*** Keywords ***

Sending Requests to the server
    ${response_objects}     ${total_null_values}    ${errors_&_count}=     process requests      ${reshape_urls}
    set global variable     ${errors_&_count}
    log                     ${response_objects}
    log                     ${total_null_values}


Verify the Response with Error(if any)
    log                     ${errors_&_count}




