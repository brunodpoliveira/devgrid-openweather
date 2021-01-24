import time
import requests

"""
- Returns:
- `1`: If
the error is handled as expected
- `0`: In other case
"""


def test_api_key():
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


def test_fetch_url():
    """
     Function to test if error handling is working for fetch url()`.
    - It's expected for fetch url to return `None`
    """
    response = ''
    if response == None:
        return 1
    return 0

    pass


def test_extract_fields_from_response():
    """
     Function to test if error handling is working`.
    - It's expected for it to return `None`
    """
    response = ''
    if response == None:
        return 1
    return 0

    pass


def test_run_program():
    """
     Function to test if error handling is working for`.
    - It's expected for it to return `None`
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
    test1 = test_fetch_url()
    if test1.response == 0:
        print('fail')
    else:
        print('sucess')
