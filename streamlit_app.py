import streamlit as st
from sentiment import analyze_sentiment

st.title("Sentilyzer - Real-Time Sentiment Analyzer")

user_input = st.text_input("Type a social media post:")
if user_input:
    result = analyze_sentiment(user_input)
    st.write(f"🧠 Sentiment: **{result}**")
