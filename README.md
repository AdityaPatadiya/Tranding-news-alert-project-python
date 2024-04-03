# Tranding-News-Alert-Project-Python
This is the news alert project that will send sms to your number. It will make you aware about the stock price for specific comapny that you looking for.

## What I've done in this project?
I used to fetch the price for the *TSLA(Tesla)* company, It will compare the currect day *market open price* price with the previous day *market closed price*. If the price is higher than 2%, then it will send formated message accordingly. Then it will also fetch the first two or three artical and send the Headline, brief and url with the message.
I used to send the no. of message according to the no. of articals.

### APIs that I used to build this project:-
1. ***For fetching the Stock Prices*** : https://www.alphavantage.co/
2. ***For fetching the news articals for given company*** : https://newsapi.org/
3. ***For sending messages*** : https://www.twilio.com/en-us

## How to automate this processes?
You receive the messages whenever you run this file, But we can automate the process that will gives you the messages every day.
Using ***pythonanywhere*** (https://www.pythonanywhere.com/), we can automate the process of sending the messages.
After sign up with this website, we can add this file and give the command that you want to run the file, and set the time accoring to your preference. With this settings, it will run that file and you will get the messages daily.
It is free with only one task at a time. You can upgrade for running more tasks at a time.

If you have anu suggessions, feel free to ensure us. Thank You✨
