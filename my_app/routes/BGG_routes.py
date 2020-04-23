from flask import Flask, Blueprint, redirect
import requests
import bs4
import lxml
from my_app.models import BGG, db

BGG_routes = Blueprint("BGG_routes", __name__)


@BGG_routes.route("/add/<game_id>/fetch")
def get_game(game_id=None):
    game_id = game_id
    url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id)
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, features='lxml')
    name = soup.find('name').text
    max_players = int(soup.find('maxplayers').text)
    min_players = int(soup.find('minplayers').text)
    playing_time = int(soup.find('playingtime').text)

    db_game = BGG.query.get(game_id) or BGG(id=game_id)
    db_game.name = name
    db_game.max_players = max_players
    db_game.min_players = min_players
    db_game.playing_time = playing_time

    db.session.add(db_game)
    db.session.commit()

    return redirect(f"/home")