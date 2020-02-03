*** Settings ***
Documentation   Importing all the supporting libs to get the request validation done
Library         RequestsLibrary
Resource        TestData/Create_URLs.robot

*** Variables ***
${my_session}
${base_url}

*** Keywords ***
1.