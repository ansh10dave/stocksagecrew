import requests 

def get_news_sentiment(ticker: str, limit=2, sort='LATEST'):
    """Fetch news sentiment for a given stock ticker or topic""" 
    api_key = "C9PMUH5UAYYXZK0J"
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={api_key}&sort=LATEST&limit={limit}"
    
    response = requests.get(url)
    data = response.json() 
    return data.get("feed", [])
