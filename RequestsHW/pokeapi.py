import requests
import time

pokemon_name = input("Please enter a pokemon name: ")

st = time.time()
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
et = time.time()

print(f"Execution time: { st - et } seconds")

print(response.json().keys())
print("\n")
print(response.json().values())

