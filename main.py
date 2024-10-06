import requests
import pprint

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'user_token' 
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}

body_out = {
   'pokemon_id':'78781' 
}

body_change_name = {
    "pokemon_id":"77560",
    "name": "TestAuto",
    "photo_id": 300
}

body_delete_pokeball = {
    'pokemon_id':'77560'
}

body_add_pokeboll = {
    'pokemon_id':'77560'
}

params ={
    'trainer_id':'6929',
    'status' : '1'
}

# Запрос POST: отправка своего покемона в накаут
response_out = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_out)
print(response_out.text)

# Запрос POST: создание нового покемона
response_create  = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create.text)

# Запрос PUT: изменить покемона
response_сhange_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_сhange_name.text)

# Запрос PUT: выселить из покебола
response_delete_pokeball = requests.put(url = f'{URL}/trainers/delete_pokeball', headers = HEADER, json = body_delete_pokeball)
print(response_delete_pokeball.text)

# Запрос POST:  поймать покемона в покебол
response_add_pokeboll =requests.post(f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeboll)
print(response_add_pokeboll.text) 

# Запрос GET: список живых покемонов по trainer_id
response_spisok_pokemonov = requests.get(url = f'{URL}/pokemons', headers = HEADER, params = params )
response_json = response_spisok_pokemonov.json()
print('Все живые покемоны тренера с trainer_id = 6929: ')
pprint.pprint(response_json)
