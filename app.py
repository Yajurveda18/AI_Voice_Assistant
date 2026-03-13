import streamlit as st
import wikipedia

st.title("AI Assistant")

user_input = st.text_input("Ask something")

if user_input:
    if "wikipedia" in user_input:
        topic = user_input.replace("wikipedia","")
        result = wikipedia.summary(topic, sentences=2)
        st.write(result)

    elif "hello" in user_input:
        st.write("Hello, how can I help you?")
