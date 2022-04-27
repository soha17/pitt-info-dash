import json
from urllib import response
import config as c
import requests
import json

def covidCheck():
    api_url = 'https://api.covidactnow.org/v2/county/42003.json?apiKey=' + c.api_key
    response = requests.get(api_url)
    json_resp = response.json()
    print('Allegheny County')
    print('Population:', "{:,}".format(int(json_resp['population'])))
    print('Weekly new cases per 100,000 people:', json_resp['metrics']['weeklyNewCasesPer100k'])
    print('CDC Transmission Level (1-4): ', json_resp['cdcTransmissionLevel'])
    