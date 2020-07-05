from bs4 import BeautifulSoup
import requests
import pandas as pd

url = requests.get("https://pokemondb.net/pokedex/all")
soup = BeautifulSoup(url.content, 'html.parser')

#DataVariables
pokemon_names = []
pokemon_hp = []
pokemon_attack = []
pokemon_defense = []
pokemon_speed = []
pokemon_types = []

names = soup.find_all('td', class_="cell-name")
for x in names:
    pokemon_names.append(x.get_text())

types = soup.find_all('td', class_="cell-icon")
for x in types:
    pokemon_types.append(x.get_text())  

other_data = []
for x in soup.find_all(attrs={'class': 'cell-num'}):
    other_data.append(x.get_text())

for i in range(1,len(other_data),7):
    pokemon_hp.append(other_data[i])

for i in range(2,len(other_data),7):
    pokemon_attack.append(other_data[i])

for i in range(3,len(other_data),7):
    pokemon_defense.append(other_data[i])

for i in range(6,len(other_data),7):
    pokemon_speed.append(other_data[i])

pokemon_hp = [int(i) for i in pokemon_hp]
pokemon_defense = [int(i) for i in pokemon_defense]
pokemon_attack = [int(i) for i in pokemon_attack]
pokemon_speed = [int(i) for i in pokemon_speed]

pokemon_data = {"NAME":pokemon_names,
        "HP":pokemon_hp,
        "ATTACK":pokemon_attack,
        "DEFENSE":pokemon_defense,
        "SPEED":pokemon_speed,
        "TYPE":pokemon_types
}

#Building a DataFrame
df = pd.DataFrame(pokemon_data)
df.to_markdown()
df.to_csv('pokedex.csv')