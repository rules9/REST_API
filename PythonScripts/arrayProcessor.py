from itertools import chain
import numpy as np


def flat_array(my_array):
    '''This creates a keyword named "flat array"

    This keyword takes one argument, which is an array and returns the flatten array
    :param my_array:
    :return: [my_array]  flatten array of urls
    '''

    # Multiplying arrays
    flatten_list = list(chain.from_iterable(my_array))
    return flatten_list

def reshape_array(url_array_recieved, batch_size):
    ''' This creates a keyword named "url array list"

    This keyword takes one argument'array', which is converted into multiple array instances and send
    back.

    :param url_array:
    :return: [urls[]]  reshaped array based on batch size, length of array, number of arrays
    '''

    # Creating URL arrays from a single array

    length_of_array = int(len(url_array_recieved))
    quotient = length_of_array // int(batch_size)
    remainder = length_of_array % int(batch_size)
    reshaped_url_array=[]
    count_of_arrays=0
    array_size=0

    if (remainder != 0 and quotient >= 1):
        for array_size in range(2,99):
            if(length_of_array % array_size ==0):
                count_of_arrays = length_of_array //array_size
                reshaped_url_array = np.reshape(url_array_recieved,(count_of_arrays,array_size))
                break
            else:
                continue
        return reshaped_url_array, length_of_array, count_of_arrays, array_size


    if (quotient==0):
        size_of_each_array =0
        reshaped_url_array = np.reshape(url_array_recieved, (remainder,1))
        return reshaped_url_array, length_of_array, (quotient+1),size_of_each_array
    else:
        reshaped_url_array = np.reshape(url_array_recieved, (quotient, int(batch_size)))
        return reshaped_url_array, length_of_array, (quotient), batch_size