import streamlit as st
import wikipedia
import speech_recognition as sr
from gtts import gTTS
from streamlit_mic_recorder import mic_recorder

st.title("AI Voice Assistant")

# -------- TEXT INPUT --------
text_input = st.text_input("Type your question")

# -------- VOICE INPUT --------
audio = mic_recorder(start_prompt="🎤 Start recording",
                     stop_prompt="⏹ Stop recording",
                     key='recorder')

voice_text = ""

if audio:
    with open("voice.wav", "wb") as f:
        f.write(audio['bytes'])

    r = sr.Recognizer()
    with sr.AudioFile("voice.wav") as source:
        audio_data = r.record(source)

    try:
        voice_text = r.recognize_google(audio_data)
        st.write("You said:", voice_text)
    except:
        st.write("Could not understand voice")

# -------- COMBINED INPUT --------
query = text_input if text_input else voice_text

if query:

    if "wikipedia" in query:
        topic = query.replace("wikipedia", "")
        result = wikipedia.summary(topic, sentences=2)

    elif "hello" in query:
        result = "Hello, how can I help you?"

    else:
        result = "I could not understand"

    st.write(result)

    # Voice output
    tts = gTTS(result)
    tts.save("answer.mp3")
    audio_file = open("answer.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")
