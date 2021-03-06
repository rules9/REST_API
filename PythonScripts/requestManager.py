import requests
from threading import  Thread
import multiprocessing as mp
from requests import get
import json
import sys



count_of_objects=0
total_null_count= 0
segment_numbers=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29''30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50']
thread_segment=[]
url_segment=[]
per_segment = 10
response_exceptions= {}
python_exception={}

#=============================================================================================Request Manager===============================

def process_requests(url_arrays):
    ''' Keyword = request processing

        This keyword process the coming URL array requests.
        Function will segregate the Requests into multithread and each thread will perform the desired task.

    :param url_arrays:
    :return: count of object in Response, Total null values in Response
    '''

    global count_of_objects
    global url_segment
    global per_segment
    global python_exception

    try:
        item_count = len(url_arrays)
        array_segment_count = item_count // per_segment
        thread_count = array_segment_count + 1
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

        if(len(response_exceptions)==0):
            response_exceptions.update({"None":0})

        return count_of_objects, total_null_count, response_exceptions


    except Exception as py_exception:
        py_exception_error = str(py_exception)
        python_exception = count_exceptions(py_exception_error, python_exception)


def request_process(segment_no):
    ''' :keyword request process

        This keword will process each of the request coming with Thread and send the
        corresponding response

    :param segment number of URL:
    :return: None
    '''


    global count_of_objects
    global total_null_count
    global python_exception
    global response_exceptions


    try:

        segment_num = int(segment_no)
        count = 0
        null_counter = 0
        response_content=''
        response=''
        count_local=''
        json_response=''
        null_counter1_local=''

        for urls_item in url_segment[segment_num]:
            for individual_url in urls_item:

                try:
                    response = requests.get(individual_url)
                    response_content = response.content

                except requests.exceptions.RequestException as process_exception:
                    process_exception_error = str(process_exception)
                    response_exceptions = count_exceptions(process_exception_error,response_exceptions)

                try:
                    count_local = int(objects_in_response(response_content))
                    json_response = response.text

                except Exception as py_exception:
                    py_exception_error = str(py_exception)
                    python_exception = count_exceptions(py_exception_error, python_exception)

                try:
                    null_counter1_local = int(count_of_null(json_response))
                    count += count_local

                except Exception as py_exception:
                    py_exception_error = str(py_exception)
                    python_exception = count_exceptions(py_exception_error, python_exception)

            null_counter += null_counter1_local

        count_of_objects = int(count_of_objects + count)
        total_null_count = int(total_null_count + null_counter)

    except Exception as py_exception:
        py_exception_error = str(py_exception)
        python_exception = count_exceptions(py_exception_error, python_exception)


#===================================================         Response Manager      ====================================================================


def objects_in_response(response_content):
    ''' Keyword object in response
        This keyword will process the response and send back
        the number of object in the response

    :param: The takes the Response content as Parameter
    :return: nubmer of objects in Response
    '''
    global python_exception

    try:
        count_of_objects_local = 0
        item_dict = json.loads(response_content)
        count_of_objects_local = len(item_dict)
        return count_of_objects_local

    except Exception as py_exception:
        py_exception_error = str(py_exception)
        python_exception = count_exceptions(py_exception_error, python_exception)


def count_of_null(response_content):
    ''' :keyword This creates the keyword as count of null
        This will count the null values in the JSON response coming

    :param response_content of response:
    :return: occurance of null object
    '''

    global python_exception
    try:
        occurance = response_content.find("null")
        return occurance

    except Exception as py_exception:
        py_exception_error = str(py_exception)
        python_exception = count_exceptions(py_exception_error, python_exception)


#=================================================================  Exception Handling ============================================

def count_exceptions(exceptions,exception_dictionary):
    ''' :keyword : This creates a keyword name count exception

        This is used to count the error present occuring

    :param exceptions:
    :param exception_dictionary:
    :return: exception dictionary with count
    '''

    if (exceptions in exception_dictionary.keys()):
        count = exception_dictionary[exceptions] +1
        exception_dictionary.update({exceptions:count})
    else:
        exception_dictionary.update({exceptions:1})

    return exception_dictionary