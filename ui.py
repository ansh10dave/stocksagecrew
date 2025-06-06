import streamlit as st  
import time 
import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
print("Python executable:", sys.executable)
from stocksagecrew.main import run

st.title("Stock News Scanner - Streaming Output") 

if st.button("🔍 Run Crew and Show Output"):
    with st.spinner("Running your agents..."):
        result = run()
        st.success("Done!")
        st.subheader("📄 Output")
        st.write(result)
else:
    print("Oh no..")