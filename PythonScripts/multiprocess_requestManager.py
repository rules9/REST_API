import requests
import  threading
import  _thread
from threading import  Thread
import multiprocessing as mp
from requests import get
import json
from   collections import Counter
from responseManager as RM



responses=[[],[]]
url_segment1=[]
url_segment2=[]
segment_numbser1=   '1'
segment_numbser2=   '2'


def request_pre_processing(url_arrays):
    '''

    :param url_arrays:
    :return:
    '''
    global url_segment1
    global url_segment2
    item_count = len(url_arrays)
    process_seg = int(item_count/2)
    url_segment1 = url_arrays[0:process_seg]
    url_segment2 = url_arrays[process_seg:item_count]

    t1 = Thread(target=call_request_processors, args=segment_numbser1, daemon=True)
    t1.start()
    # t2 = Thread(target=call_request_processors, args=segment_numbser2, daemon=True)
    # t2.start()

    t1.join()
    # t2.join()

def call_request_processors(url_seg):
    request_process(url_seg)



def request_process(segment):
    '''

    '''
    segment_num = int(segment)
    global responses
    if (segment_num ==1):
        for urls_item in url_segment1:
            for individual_url in urls_item:
                response = requests.get(individual_url)
                response_content = response.content
                # responses.append(response_content)
                object_in_response(response_content)
                break
            break

    if (segment_num == 2):
        for urls_item in url_segment2:
            for individual_url in urls_item:
                response = requests.get(individual_url)
                response_content = response.content
                responses.append(response_content)
                break
            break








# def process_request(url_array,seg_number):
#     t1 = Thread(target=call_request_process,args=seg_number,daemon=True)
#     t1.start()
#     t2 = Thread(target=call_request_process, args=seg_number,daemon=True)
#     t2.start()
#     return responses



