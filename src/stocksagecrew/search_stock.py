import requests 

def ask_ollama(prompt: str, model="gemma3:4b"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()  # will raise an error for 4xx/5xx
    return response.json()["response"]

def get_stock_symbol(company: str):
    import os
    import requests

    api_key = 'C9PMUH5UAYYXZK0J'
    url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company}&apikey={api_key}"
    r = requests.get(url)
    r.raise_for_status()
    results = r.json()["bestMatches"]
    display = [
        f"{match['2. name']} ({match['1. symbol']}) — Region: {match['4. region']}"
        for match in results[:3]
    ]
    symbol = results[0]['1. symbol']

    return display, symbol

def get_stock_info(symbol: str) -> dict:
    api_key = 'C9PMUH5UAYYXZK0J'
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    r = response.json()
    return r

def run_stock_check(user_prompt: str):
    company = ask_ollama(f"""Extract only the company name from this sentence. No explanation.
    Sentence: "{user_prompt}" Company:""")
    
    display, symbol = get_stock_symbol(company.strip())
    stock_info = get_stock_info(symbol) if symbol else {}
    return company, display, symbol, stock_info




