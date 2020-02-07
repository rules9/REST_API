import csv
import sys

def read_csv_file(filename):
    '''This creates a keyword named "Read CSV File"

    This keyword takes one argument, which is a path to a .csv file. It
    returns a list of rows, with each row being a list of the data in
    each column.
    :param : File address
    :return: Array data of url
    '''
    try:
        data=[]
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data
    except Exception as csv_exception:
            exe_info = sys.exc_info()

def verify_array(variable,filename):
    ''' This creates a keyword "verify URL array"

    This function will verify all the array created by the
    read csv file keyword.
    :param : File address
    :return: True/Flase based on the content
    '''

    try:
        data = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return (variable == data)
    except Exception as csv_exception:
            exe_info = sys.exc_info()


