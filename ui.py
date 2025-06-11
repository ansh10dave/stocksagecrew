import streamlit as st  
import time 
import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
print("Python executable:", sys.executable)
from stocksagecrew.main import run
from stocksagecrew.search_stock import run_stock_check
import streamlit.components.v1 as components 
from stocksagecrew.market_news import get_news_sentiment

st.title("Stock News Scanner - Streaming Output") 

if st.button("🔍 Run Crew and Show Output"):
    with st.spinner("Running your agents..."):
        result = run()
        st.success("Done!")
        st.subheader("📄 Output")
        st.write(result)
else:
    print("Oh no..")

st.subheader("Stock Lookup Assistant") 

user_input = st.text_input("Ask about a company's stock:", "")
num_articles = st.slider("Number of artices", min_value=1, max_value=20, value=10)

if st.button("Check stock info and get news"):
    if user_input:
        with st.spinner("Getting stock data..."):
            try:
                company, display, symbol, stock_info = run_stock_check(user_input)
                st.markdown(f"🔍 Results for: {company.strip()}")
                if stock_info:
                    st.subheader("📈 Stock Information")
                    # quote = stock_info.get("Global Quote", {})
                    # st.write(f"**Symbol:** {quote.get('01. symbol', 'N/A')}")
                    # st.write(f"**Price:** ${quote.get('05. price', 'N/A')}")
                    # st.write(f"**Change:** {quote.get('09. change', 'N/A')}")
                    # st.write(f"**Change Percent:** {quote.get('10. change percent', 'N/A')}")
                    # st.write(f"**Latest Trading Day:** {quote.get('07. latest trading day', 'N/A')}")
                    def show_tradingview_chart(symbol: str):
                        tradingview_html = f"""
                        <iframe src="https://www.tradingview.com/widgetembed/?symbol={symbol}&interval=D&hidesidetoolbar=1&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=[]&theme=light&style=1&timezone=Etc/UTC&withdateranges=1&hideideas=1"
                        width="100%" height="500" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
                        """
                        components.html(tradingview_html, height=500)

                    st.subheader(f"Live Stock Chart for {company}")
                    show_tradingview_chart(symbol)
                    st.subheader("Latest news")
                    with st.spinner("Fetching news..."):
                        articles = get_news_sentiment(symbol.upper(), limit=2)
                        target_ticker = symbol.upper()
                        articles = [
                            article for article in articles if any(t.get("ticker") == target_ticker for t in article.get("ticker_sentiment", []))
                               ]
                        articles = articles[:num_articles]
                        
                    if not articles:
                        st.warning("No news found for the given ticker.")
                    else:
                        for article in articles:
                            sentiment = article.get("overall_sentiment_label", "N/A")
                            color = {"Positive": "green", "Neutral": "gray", "Negative": "red"}.get(sentiment, "blue")
    
                            tickers = [t.get("ticker", "N/A") for t in article.get("ticker_sentiment", [])]
                            with st.container():
                                st.markdown(f"### [{article['title']}]({article['url']})")
                                st.markdown(f"**Summary:** {article['summary']}")
                                st.markdown(f"<span style='color:{color}; font-weight:bold'>Sentiment: {sentiment}</span>", unsafe_allow_html=True)
                                st.markdown(f"**Related Tickers:** {', '.join(tickers)}") 
                                st.markdown("---")

                else:
                    st.warning("No stock information available.")

            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter a prompt.")





