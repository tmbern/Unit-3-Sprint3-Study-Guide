from flask import Flask, Blueprint, redirect
import requests
from my_app.models import Stocks, db
import json

stocks_routes = Blueprint("stocks_routes", __name__)

@stocks_routes.route("/add_stocks/<stock_symbol>/fetch")
def get_stock(stock_symbol=None):
    """get a daily return of a given stock from the Alpha Vantage API
       takes those returns and iterates thru them to add them to our 'Stocks' Database

    Keyword Arguments:
        stock_symbol {[string: like TSLA]} -- [the official ticker symbol for a stock] (default: {None})
    """
    API_KEY = "J36ROGE9ELUSMRH4"
    STOCK_SYMBOL= stock_symbol
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_SYMBOL}&apikey={API_KEY}"

    # gets the request to the above api from Alpha Vantage
    response = requests.get(request_url)

    # loads the json object to text
    parsed_response = json.loads(response.text)

    # get just the daily prices without the metadata
    daily_prices = parsed_response["Time Series (Daily)"]

    for daily in daily_prices:
        db_stock = Stocks.query.get(STOCK_SYMBOL) or Stocks(name=STOCK_SYMBOL)
        db_stock.date = daily
        db_stock.open_ = float(daily_prices[daily]["1. open"])
        db_stock.high_ = float(daily_prices[daily]["2. high"])
        db_stock.low_ = float(daily_prices[daily]["3. low"])
        db_stock.close_ = float(daily_prices[daily]["4. close"])
        db.session.add(db_stock)
    db.session.commit()

    return redirect(f"/home")         
