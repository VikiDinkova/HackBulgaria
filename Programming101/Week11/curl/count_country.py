# from simple_http_server import *
import requests

airlines = requests.get('http://astral.hacksoft.io/api/airline/?format=json')
country_list = requests.get('http://data.okfn.org/data/core/country-list/r/data.json')

airlines = airlines.json()
country_list = country_list.json()

country = 'Bulgaria'

count = 0

for airline in airlines:
    for cou in country_list:
        if cou['Name'] == country:
            if airline['country_code'] == cou['Code']:
                count += 1
print(count)
