from itertools import chain
def process_array(my_array):
    '''This creates a keyword named "process array"

    This keyword takes one argument, which is an array and returns the flatten array
    '''

    # Multiplying arrays
    flatten_list = list(chain.from_iterable(my_array))
    return flatten_list