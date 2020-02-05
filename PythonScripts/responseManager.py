import requests
import json

def objects_in_response(response_content):
    '''


    :return:
    '''

    count_of_objects=99
    json_data = json.dumps(response_content)
    item_dict = json.loads(json_data)
    count_of_objects =len(item_dict)

    return count_of_objects