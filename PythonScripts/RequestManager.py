import requests

def request_hit():
    '''

    '''
    URL = 'https://bit.ly/2MMhOhs'
    r = requests.get(url=URL)
    print(r)
    data = r.json()
    return data
