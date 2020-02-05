import requests
import  threading
import  _thread
from threading import  Thread
import multiprocessing as mp
from requests import get


def request_process(url_arrays):
    '''

    '''
    item_count = len(url_arrays)
    index =0
    resposes=[]
    for urls_item in url_arrays:
        for individual_url in urls_item:
            response = requests.get(individual_url)
            response_content = response.content
            resposes.append(response_content)

    return resposes
