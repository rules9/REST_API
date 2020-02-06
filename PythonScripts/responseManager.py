import requests
from threading import  Thread
import multiprocessing as mp
from requests import get
import json


count_of_objects=0
total_null_count= 0
segment_numbers=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29''30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50']
thread_segment=[]
url_segment=[]
per_segment = 15

def request_pre_processing(url_arrays):
    '''

    :param url_arrays:
    :return:
    '''

    global count_of_objects
    global url_segment
    global per_segment

    item_count = len(url_arrays)
    array_segment_count = item_count//per_segment
    thread_count = array_segment_count +1
    array_segment_remainder = item_count % per_segment
    previous_segment_count = 0



    if (array_segment_count==0):
        url_segment_raw = (url_arrays[0:item_count])
        url_segment.append(url_segment_raw)
    else:
        for item in range(array_segment_count):
            url_segment_raw = (url_arrays[previous_segment_count:per_segment])
            url_segment.append(url_segment_raw)
            previous_segment_count = per_segment
            per_segment += per_segment
        if (array_segment_remainder != 0):
            url_segment_raw = (url_arrays[previous_segment_count:item_count])
            url_segment.append(url_segment_raw)


    for item in range(thread_count):
        thread_raw = 'thread_' + str(item)
        thread_segment.append(thread_raw)
        thread_segment[item] = Thread(target=request_process, args=segment_numbers[item], daemon=True)
        thread_segment[item].start()

    for item in range(thread_count):
        thread_segment[item].join()

    return count_of_objects,total_null_count


def request_process(segment_no):
    '''

    '''

    segment_num = int(segment_no)
    global count_of_objects
    global total_null_count

    count = 0
    null_counter=0

    for urls_item in url_segment[segment_num]:
        for individual_url in urls_item:
            response = requests.get(individual_url)
            response_content = response.content
            count_local = int(objects_in_response(response_content))
            json_response = response.text
            null_counter1_local = int(count_of_null(json_response))
            count+= count_local
            null_counter+=null_counter1_local


    count_of_objects = int(count_of_objects + count)
    total_null_count = int(total_null_count + null_counter)


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