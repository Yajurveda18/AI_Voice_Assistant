import streamlit as st
import wikipedia
from gtts import gTTS

st.title("AI Voice Assistant")

user_input = st.text_input("Ask something")

if user_input:

    if "wikipedia" in user_input:
        topic = user_input.replace("wikipedia","")
        result = wikipedia.summary(topic, sentences=2)

    elif "hello" in user_input:
        result = "Hello, how can I help you?"

    else:
        result = "I could not understand"

    st.write(result)

    # Convert text to speech
    tts = gTTS(result)
    tts.save("voice.mp3")

    # Play audio in browser
    audio_file = open("voice.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")
