import time
import requests

"""
- Returns:
- `1`: If
the error is handled as expected
- `0`: In other case
"""


def bad_api_key():
    """
     Function to test if error handling is working
      for all functions that requires an API Key to make a request`.
    - It's expected for fetch url to return `None`
    """
    response = ''
    if response == None:
        return 1
    return 0

    pass


def bad_adress():
    """
     Function to test if error handling is working for fetch url()`.
    - It's expected for fetch url to return `None`
    """
    response = ''
    if response == None:
        return 1
    return 0

    pass


def everything_wrong():
    """
    test to check if everything behaves when more than one thing fails at the same time.
    Here we try to request forecast information of from non existing web site with a bad API Key.
    """
    response = ''
    if response == None:
        return 1
    return 0

    pass


if __name__ == '__main__':
    print('Test began')
    test = bad_api_key()
    if test.response == 0:
        print('fail')
    else:
        print('sucess')

    #test2 = bad_adress()
    #test3 = everything_wrong()
