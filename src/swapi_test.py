from test_cases import *
import requests
import time


def test_response(api_url, expected_status_code, response_timeout, expected_body):
    t1 = time.perf_counter()
    response = requests.get(api_url)
    t2 = time.perf_counter()

    response_url = response.url
    print(f'URL: {response_url}')

    actual_status_code = response.status_code
    if actual_status_code == expected_status_code:
        print(f'Status code: {actual_status_code} - OK')
    else:
        print(f'Status code: {actual_status_code} - Does not match')

    response_time = t2-t1
    if response_time < response_timeout:
        print(f'Response time: {response_time} Seconds - OK')
    else:
        print(f'Response time: {response_time} Seconds - Response timeout Exceeded')

    actual_response_body = response.json()
    if actual_response_body == expected_body:
        print(f'Response body - OK')
    else:
        print(f'Response body - Does not match')
        print(f'Actual Response body: {actual_response_body}')
        # print(f'Expected Response body: {expected_body}')

    print(f'\n================\n')


for case in test_cases:
    test_response(case.api_url, case.expected_status_code, case.response_timeout, case.expected_body)
