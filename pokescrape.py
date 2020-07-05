{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import pandas as pd\n",
    "\n",
    "url = requests.get(\"https://pokemondb.net/pokedex/all\")\n",
    "soup = BeautifulSoup(url.content, 'html.parser')\n",
    "\n",
    "#DataVariables\n",
    "pokemon_names = []\n",
    "pokemon_hp = []\n",
    "pokemon_attack = []\n",
    "pokemon_defense = []\n",
    "pokemon_speed = []\n",
    "pokemon_types = []\n",
    "\n",
    "names = soup.find_all('td', class_=\"cell-name\")\n",
    "for x in names:\n",
    "    pokemon_names.append(x.get_text())\n",
    "\n",
    "types = soup.find_all('td', class_=\"cell-icon\")\n",
    "for x in types:\n",
    "    pokemon_types.append(x.get_text())  \n",
    "\n",
    "other_data = []\n",
    "for x in soup.find_all(attrs={'class': 'cell-num'}):\n",
    "    other_data.append(x.get_text())\n",
    "\n",
    "for i in range(1,len(other_data),7):\n",
    "    pokemon_hp.append(other_data[i])\n",
    "\n",
    "for i in range(2,len(other_data),7):\n",
    "    pokemon_attack.append(other_data[i])\n",
    "\n",
    "for i in range(3,len(other_data),7):\n",
    "    pokemon_defense.append(other_data[i])\n",
    "\n",
    "for i in range(6,len(other_data),7):\n",
    "    pokemon_speed.append(other_data[i])\n",
    "\n",
    "pokemon_hp = [int(i) for i in pokemon_hp]\n",
    "pokemon_defense = [int(i) for i in pokemon_defense]\n",
    "pokemon_attack = [int(i) for i in pokemon_attack]\n",
    "pokemon_speed = [int(i) for i in pokemon_speed]\n",
    "\n",
    "pokemon_data = {\"NAME\":pokemon_names,\n",
    "        \"HP\":pokemon_hp,\n",
    "        \"ATTACK\":pokemon_attack,\n",
    "        \"DEFENSE\":pokemon_defense,\n",
    "        \"SPEED\":pokemon_speed,\n",
    "        \"TYPE\":pokemon_types\n",
    "}\n",
    "\n",
    "#Building a DataFrame\n",
    "df = pd.DataFrame(pokemon_data)\n",
    "df.to_csv('pokedex.csv') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
