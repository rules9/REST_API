import csv

def read_csv_file(filename):
    '''This creates a keyword named "Read CSV File"

    This keyword takes one argument, which is a path to a .csv file. It
    returns a list of rows, with each row being a list of the data in
    each column.
    '''
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def verify_array(variable,filename):
    ''' This creates a keyword "verify URL array"

    This function will verify all the array created by the
    read csv file keyword.
    '''
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    return (variable == data)
