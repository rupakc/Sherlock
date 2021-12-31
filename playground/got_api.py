import requests
from fastapi import FastAPI, Body
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()


def get_list_of_got_entities(base_url="https://www.anapioficeandfire.com/api/", entity_type='books'):
    """

    :param base_url:
    :param entity_type: Can be one of the following - books, houses, characters
    :return:
    """
    final_url = base_url + entity_type
    response_list = []
    response = requests.get(final_url)
    if response.status_code == 200:
        response_list = response.json()
    return response_list


def get_summary_of_covid_cases(url='https://api.covid19api.com/summary'):
    """

    :param url:
    :return:
    """
    response_json = ''
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
    return response_json


def get_age_of_empires_attributes(base_url='https://age-of-empires-2-api.herokuapp.com/api/v1/', entity_type='civilizations'):
    """

    :param base_url:
    :param entity_type: Can be one of the following - structures, civilizations, technologies, units
    :return:
    """
    final_url = base_url + entity_type
    response_json = ''
    response = requests.get(final_url)
    if response.status_code == 200:
        response_json = response.json()
    return response_json


# print(get_age_of_empires_attributes(entity_type='technologies'))
# print(get_list_of_got_entities(entity_type='characters'))

@app.get("/v1/covid")
def get_latest_covid_summary_report():
    return get_summary_of_covid_cases()


@app.get("/v1/ageofempires")
def get_age_of_empires_data(entity_type="civilizations"):
    return get_age_of_empires_attributes(entity_type=entity_type)


@app.get("/v1/gameofthrones")
def get_game_of_thrones_data(entity_type="books"):
    return get_list_of_got_entities(entity_type=entity_type)


