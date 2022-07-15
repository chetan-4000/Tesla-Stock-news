from twilio.rest import Client
import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

twilio_account_sid = "**************************"
twilio_auth_token = "***************************"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stk_api_k = "QA8N8RD9V8HJR1CE"
nws_api_k = "0e15153f823a4f73b8e0bd33ddd150c3"
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stk_p = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":stk_api_k
}

response = requests.get(url=STOCK_ENDPOINT,params=stk_p)
stk_end = response.json()["Time Series (Daily)"]
stk_end_list =[value for (key,value)in stk_end.items()]
yesterday_close_price = stk_end_list[0]["4. close"]
a=float(yesterday_close_price)

day_before_close = stk_end_list[1]["4. close"]
b = float(day_before_close)

diffrence = abs(b-a)

per_diff = (diffrence/(a+b)/2)*100

if per_diff > 0:
    nws_params = {
        "apiKey":nws_api_k,
        "qInTitle":COMPANY_NAME,
    }
    response1 = requests.get(url=NEWS_ENDPOINT,params=nws_params)
    news = response1.json()["articles"]
    three_news = news[:3]


    final_news = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_news]
    client = Client(twilio_account_sid, twilio_auth_token)

    for article in final_news:
        message = client.messages.create(
            body=article,
            from_='*********',
            to='*********'
        )



