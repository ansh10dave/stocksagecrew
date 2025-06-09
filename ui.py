import streamlit as st  
import time 
import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
print("Python executable:", sys.executable)
from stocksagecrew.main import run
from stocksagecrew.search_stock import run_stock_check

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
                company, result = run_stock_check(user_input)
                st.subheader(f"🔍 Results for: {company.strip()}")
                if result:
                    for entry in result:
                        st.markdown(f"- {entry}")
                else:
                    st.warning("No matches found.")
            except Exception as e:
                st.error(f"❌ Error: {e}")

            #     # Check that result is a dict and has 'bestMatches'
            #     if isinstance(result, dict) and result.get("bestMatches"):
            #         best_matches = result["bestMatches"]
            #         if best_matches:
            #             for match in best_matches:
            #                 symbol = match.get("1. symbol", "N/A")
            #                 name = match.get("2. name", "N/A")
            #                 region = match.get("4. region", "N/A")
            #                 currency = match.get("8. currency", "N/A")
            #                 match_score = match.get("9. matchScore", "N/A")

            #                 st.markdown(f"""
            #                 **Symbol:** `{symbol}`  
            #                 **Name:** {name}  
            #                 **Region:** {region}  
            #                 **Currency:** {currency}  
            #                 **Match Score:** {match_score}
            #                 """)
            #                 st.markdown("---")
            #         else:
            #             st.warning("No matches found.")
            #     else:
            #         st.warning("No results or unexpected response format.")
            # except Exception as e:
            #     st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter a prompt.")

