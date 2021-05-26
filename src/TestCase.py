class TestCase:
    def __init__(self, api_url, expected_status_code, response_timeout, expected_body):
        self.api_url = api_url
        self.expected_status_code = expected_status_code
        self.response_timeout = response_timeout
        self.expected_body = expected_body
