import requests
from bs4 import BeautifulSoup

url = "https://keeptradecut.com/dynasty-rankings"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

player_elements = soup.find_all('div', class_='onePlayer')

count = 0

for player in player_elements:
    name = player.find('p', class_='player-name').text
    pos = player.find('p', class_='position').text
    age = player.find('p', class_='age')
    if age and age.text:
        age = age.text
    value = player.find('p', class_='value').text    
    print(name, pos, age, value)
    count+=1

print(count)