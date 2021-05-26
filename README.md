#The Star Wars API Test

[SWAPI - The Star Wars API](https://swapi.dev/ "SWAPI - The Star Wars API")

##Read API-documentation
[API-documentation](https://swapi.dev/documentation "SWAPI - The Star Wars API")
##Install pipenv and requests

Windows, CMD as administrator:
<!-- UL -->
* pip --version
* python -m pip install --upgrade pip
* pip install --user pipenv

Add to User variables PATH:
<!-- UL -->
* C:\Users\root\AppData\Roaming\Python\Python39\Scripts

##Add some cases to test_cases.py

<!-- UL -->
* _api_url, 
expected_status_code, 
response_timeout, 
expected_body_
```python
test_cases = [
    TestCase("https://swapi.dev/api/films/1/", 200, 1, "{'title': 'A New Hope', 'episode_id': 4,"
    TestCase("https://swapi.dev/api/films/2/", 200, 1, "{'title': 'The Empire Strikes Back', 'episode_id': 5,"
    TestCase("https://swapi.dev/api/films/3/", 200, 1, "{'title': 'Return of the Jedi', 'episode_id': 6,"
    TestCase("https://swapi.dev/api/films/4/", 200, 1, "{'title': 'The Phantom Menace', 'episode_id': 1,"
    TestCase("https://swapi.dev/api/films/5/", 200, 1, "{'title': 'Attack of the Clones', 'episode_id': 2,"
    TestCase("https://swapi.dev/api/films/6/", 200, 1, "{'title': 'Revenge of the Sith', 'episode_id': 3,"
]
```

##Run swapi_test.py
```python
URL: https://swapi.dev/api/films/1/
Status code: 200 - OK
Response time: 0.3216488 Seconds - OK
Response body - OK

================

URL: https://swapi.dev/api/films/2/
Status code: 200 - OK
Response time: 0.21584589999999998 Seconds - OK
Response body - OK

================

URL: https://swapi.dev/api/films/3/
Status code: 200 - OK
Response time: 0.22247299999999992 Seconds - OK
Response body - OK

================

URL: https://swapi.dev/api/films/4/
Status code: 200 - OK
Response time: 0.3670886 Seconds - OK
Response body - OK

================

URL: https://swapi.dev/api/films/5/
Status code: 200 - OK
Response time: 0.4660104999999999 Seconds - OK
Response body - OK

================

URL: https://swapi.dev/api/films/6/
Status code: 200 - OK
Response time: 0.2732199000000002 Seconds - OK
Response body - OK

================


Process finished with exit code 0
```

