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
total_null_count= 0

def request_pre_processing(url_arrays):
    '''

    :param url_arrays:
    :return:
    '''

    global url_segment1
    global url_segment2
    global count_of_objects

    item_count = len(url_arrays)

    url_segment1 = url_arrays[0:6]
    url_segment2 = url_arrays[2:item_count]

    t1 = Thread(target=call_request_processors, args=segment_number1, daemon=True)
    t1.start()
    # t2 = Thread(target=call_request_processors, args=segment_number2, daemon=True)
    # t2.start()
    # t2.join()
    t1.join()


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
    global url_segment1
    global url_segment2

    count1 = 0
    count2 = 0
    null_counter2=0
    null_counter1=0

    if (segment_num == 1):
        for urls_item in url_segment1:
            for individual_url in urls_item:
                response = requests.get(individual_url)
                response_content = response.content
                count1_local = int(objects_in_response(response_content))
                json_response = response.text
                null_counter1_local = int(count_of_null(json_response))
                count1+= count1_local
                null_counter1+=null_counter1_local

    if (segment_num == 2):
        for urls_item in url_segment2:
            for individual_url in urls_item:
                response = requests.get(individual_url)
                response_content = response.content
                count2 = int(objects_in_response(response_content))
                json_response = response.text
                null_counter2 = int(count_of_null(json_response))
            count2 += count2
            null_counter2 += null_counter2

    count_of_objects = int(count_of_objects + count1 + count2)
    total_null_count = int(total_null_count + null_counter1 + null_counter2)


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
    '''


    :param response_content:
    :return:
    '''
    occurance = response_content.find("null")
    return occurance