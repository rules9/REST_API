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



def reshape_array(url_array,batch_size):
    ''' This creates a keyword named "url array list"

    This keyword takes one argument'array', which is converted into multiple array instances and send
    back.

    :param url_array:
    :return: [urls[]]  reshaped array based on batch size, length of array, number of arrays
    '''

    #Creating URL arrays from a single array

    length_of_array = int(len(url_array))
    quotient = length_of_array//int(batch_size)
    remainder = length_of_array%int(batch_size)

    if(remainder!=0):
        url_array = url_array[:((length_of_array)-remainder)]
        url = np.reshape(url_array,(quotient, int(batch_size)))
        return url,length_of_array,quotient

    else:
        url = np.reshape(url_array, (quotient, int(batch_size)))
        return url, length_of_array, quotient