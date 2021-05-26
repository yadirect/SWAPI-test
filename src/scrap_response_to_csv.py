import requests
import csv

resources = [
    "people",
    "planets",
    "films",
    "species",
    "vehicles",
    "starships",
]

# People: 82
# Planets: 60
# Films: 6
# Species : 37
# Vehicles: 39
# Starships: 36


def response_to_list(resource, num):
    result = []
    item_num = 1
    for i in range(num):
        custom_url = f'https://swapi.dev/api/{resource}/{item_num}/'
        response = requests.get(custom_url)
        response_url = response.url
        status_code = response.status_code
        response_body = response.json()
        person = {
                    'response_url': f'{response_url}',
                    'status_code': f'{status_code}',
                    'response_body': f'{response_body}',
                }
        result.append(person)
        item_num += 1
    return result


responses = response_to_list("films", 6)

for line in responses:
    print(line)

with open('responses.csv', 'w', newline='') as new_file:
    fieldnames = ['response_url', 'status_code', 'response_body']

    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

    csv_writer.writeheader()

    for line in responses:
        csv_writer.writerow(line)
