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

    return [
        f"{match['2. name']} ({match['1. symbol']}) — Region: {match['4. region']}, Match Score: {match['9. matchScore']}"
        for match in results[:3]
    ]

def run_stock_check(user_prompt: str):
    company = ask_ollama(f"""Extract only the company name from this sentence. No explanation.
    Sentence: "{user_prompt}" Company:""")
    
    results = get_stock_symbol(company.strip())
    return company, results

# Example usage:
user_prompt = "How is Nvidia doing?"
a=run_stock_check(user_prompt)
print(a)