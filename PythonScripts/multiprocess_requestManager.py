import requests
import  threading
import  _thread
from threading import  Thread
import multiprocessing as mp
from requests import get
import json
from   collections import Counter



responses=''
url_segment1=[]
url_segment2=[]
segment_number1=   '1'
segment_number2=   '2'
count_of_objects=0
total_null_count=0

def request_pre_processing(url_arrays):
    '''

    :param url_arrays:
    :return:
    '''

    global url_segment1
    global url_segment2
    global count_of_objects

    item_count = len(url_arrays)

    url_segment1 = url_arrays[0:1]
    url_segment2 = url_arrays[1:item_count]

    t1 = Thread(target=call_request_processors, args=segment_number1, daemon=True)
    t1.start()
    t2 = Thread(target=call_request_processors, args=segment_number2, daemon=True)
    t2.start()

    t1.join()
    t2.join()

    return count_of_objects , total_null_count

def call_request_processors(url_seg_number):
    request_process(url_seg_number)



def request_process(segment_no):
    '''

    '''

    segment_num = int(segment_no)
    global responses
    global count_of_objects
    global total_null_count

    count1 = 0
    count2 = 0
    null_counter1 =0
    null_counter2=0

    if (segment_num == 1):
        for urls_item in url_segment1:
            for individual_url in urls_item:
                response = requests.get(individual_url)
                response_content = response.content
                count1 = objects_in_response(response_content)
                null_counter1 = count_of_null(response_content)
                break
            break

    if (segment_num == 2):
        for urls_item in url_segment2:
            for individual_url in urls_item:
                response = requests.get(individual_url)
                response_content = response.content
                count2 = objects_in_response(response_content)
                null_counter2 = count_of_null(response_content)
                break
            break

    count_of_objects = count_of_objects+ count1 + count2
    total_null_count = total_null_count +null_counter1+null_counter2


# def process_request(url_array,seg_number):
#     t1 = Thread(target=call_request_process,args=seg_number,daemon=True)
#     t1.start()
#     t2 = Thread(target=call_request_process, args=seg_number,daemon=True)
#     t2.start()
#     return responses

#=============================================================================================Response Manager===============================



def objects_in_response(response_content):
    '''


    :return:
    '''

    count_of_objects_local =0
    item_dict = json.loads(response_content)
    count_of_objects_local =len(item_dict)
    return count_of_objects_local



def count_of_null(response_content):
    null_count = 0
    jsondata = json.loads(response_content)

    return jsondata