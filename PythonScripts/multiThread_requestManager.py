
#================= For Multithreading ===============================================

#     for item in range(0,(item_count-1)):
#         url = url_arrays[index]
#         t = Thread(target=request_hit, args=(url,))
#         t.start()
#         response = t.join()
#         #_thread.start_new_thread(request_hit,(url,))
#         responses.append(response)
#         index = index +1
#         return responses
#
#
# def request_hit(url_array):
#     sub_responses=[]
#     for individual_url in url_array:
#         response = requests.get(individual_url)
#         sub_responses.append(response)
#     return sub_responses
#=============================================================================================================================