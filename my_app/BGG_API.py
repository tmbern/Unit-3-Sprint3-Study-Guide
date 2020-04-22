from flask import Flask
import requests
import bs4
import lxml

game_id = 13
url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id)
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, features='lxml')
print(soup.find('name').text)
print("min players", soup.find('minplayers').text)
print("max players", soup.find('maxplayers').text)
print("avg playing time", soup.find('playingtime').text)
print('basic game play?')
print(soup.find('description').text)