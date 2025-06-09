import streamlit as st  
import time 
import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
print("Python executable:", sys.executable)
from stocksagecrew.main import run
from stocksagecrew.search_stock import run_stock_check
import streamlit.components.v1 as components 

st.title("Stock News Scanner - Streaming Output") 

if st.button("🔍 Run Crew and Show Output"):
    with st.spinner("Running your agents..."):
        result = run()
        st.success("Done!")
        st.subheader("📄 Output")
        st.write(result)
else:
    print("Oh no..")

st.markdown("Stock Lookup Assistant") 

user_input = st.text_input("Ask about a company's stock:", "")

if st.button("Check"):
    if user_input:
        with st.spinner("Getting stock data..."):
            try:
                company, display, symbol, stock_info = run_stock_check(user_input)
                st.subheader(f"🔍 Results for: {company.strip()}")
                if display:
                    for entry in display:
                        st.markdown(f"- {entry}")
                else:
                    st.warning("No matches found.")
                if stock_info:
                    st.subheader("📈 Stock Information")
                    quote = stock_info.get("Global Quote", {})
                    st.write(f"**Symbol:** {quote.get('01. symbol', 'N/A')}")
                    st.write(f"**Price:** ${quote.get('05. price', 'N/A')}")
                    st.write(f"**Change:** {quote.get('09. change', 'N/A')}")
                    st.write(f"**Change Percent:** {quote.get('10. change percent', 'N/A')}")
                    st.write(f"**Latest Trading Day:** {quote.get('07. latest trading day', 'N/A')}")
                    def show_tradingview_chart(symbol: str):
                        tradingview_html = f"""
                        <iframe src="https://www.tradingview.com/widgetembed/?symbol={symbol}&interval=D&hidesidetoolbar=1&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=[]&theme=light&style=1&timezone=Etc/UTC&withdateranges=1&hideideas=1"
                        width="100%" height="500" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
                        """
                        components.html(tradingview_html, height=500)

                    st.subheader(f"Live Stock Chart for {company}")
                    show_tradingview_chart(symbol)

                else:
                    st.warning("No stock information available.")

            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter a prompt.")





