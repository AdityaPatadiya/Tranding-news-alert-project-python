import requests
import time
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "YOUR_API_KEY_FOR_STOCK_API"
}
stock_news_api_params = {
    "q": COMPANY_NAME,
    "apikey": "YOUR_API_FOR_NEWS_API"
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

responce_for_price = requests.get(STOCK_ENDPOINT, params=stock_api_params)
responce_for_news = requests.get(NEWS_ENDPOINT, params=stock_news_api_params)
responce_for_price.raise_for_status()
responce_for_news.raise_for_status()

stock_price_all_data = responce_for_price.json()
Daily_Stock_Prise = stock_price_all_data["Time Series (Daily)"]

first_day = next(iter(Daily_Stock_Prise))
first_day_values = Daily_Stock_Prise.pop(first_day)  # it will retrieve the first element and pop(means it will remove
# that first pair) and the next time we again get the first pair.
first_day_price = first_day_values["4. close"]

second_day = next(iter(Daily_Stock_Prise))
second_day_values = Daily_Stock_Prise[second_day]
second_day_price = second_day_values["1. open"]

# IT WILL CONVERT DICTIONARY INTO THE TUPLE
# first_day = Daily_Stock_Prise.popitem()  # it will convert the dictionary into the tuple
# print(first_day)
# print(first_day[1]["4. close"])

first_article = []
difference = float(second_day_price) - float(first_day_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

different_percent = round(((difference/float(first_day_price))*100))

if abs(different_percent) > 2:  # abs is used to return the absolute valus means it number is negative then it return the positive number.
    stock_news_all_data = responce_for_news.json()["articles"]
    for n in range(0, 3):
        first_article.append(stock_news_all_data[n]["url"])
    three_articles = stock_news_all_data[:3]
    formatted_articles = [f"{STOCK}: {up_down}{different_percent}%\nHeadline: {article["title"]}. \n\nBrief: {article["description"]}. \n\nURL: \n{article["url"]}" for article in three_articles]

    for i in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=i,
            from_="[ENTER THE NUMBER FROM TWILLIO WEBSITE.]",
            to="[THE NUMBER TO THAT YOU WANT TO SEND THE MESSAGE]"
        )
