import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6c39f8478effc9a185036981100466b0' 
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '6929'

def test_status_code():
   response_get_trainers = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
   assert  response_get_trainers.status_code == 200
   
def test_sattus_code_list_pokemons():
   response_get_pokemons = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
   assert response_get_pokemons.status_code == 200
     
def test_trainer_name():
   response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
   assert response_name.json()['data'][0]['trainer_name'] == 'Samaritynin'
   
def test_trainer_city():
   response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
   assert response_name.json()['data'][0]['city'] == 'Самара'
   
@pytest.mark.parametrize('key, value', [('id','77560'),('name','TestAuto'),('trainer_id', TRAINER_ID)])
def test_parametrize(key, value):
   response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
   assert response_parametrize.json()["data"][11][key] == value   
   
   
