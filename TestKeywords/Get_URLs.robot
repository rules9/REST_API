*** Settings ***
Documentation   Importing all the supporting libs to get the request validation done
Library         RequestsLibrary
Resource        TestData/URLs.robot

*** Variables ***
${my_session}
${base_url}     url1

*** Keywords ***
1.