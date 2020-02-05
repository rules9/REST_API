#    create session   my_session  ${url}     verify=True
#    ${response}=        GET REQUEST    my_session     ${url}    allow_redirects=${True}
#    log to console      ${response.status_code}
#    :FOR    ${url}  IN  @{urls}
#        \   LOG                 ${url}
#        \   ${response}=        get request    my_session     ${url}
#        \   log to console      ${response.status_code}
#        \   append to list      ${responses}    ${response}
#        \   LOG                 ${responses}




#
#    :FOR    ${urls1}    IN      @{urls}
#    \   ${response}=    request_process     ${urls}
#    \   log to console      ${response}
#    \   log                 ${response}