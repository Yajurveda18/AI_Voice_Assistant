import streamlit as st
import wikipedia
import speech_recognition as sr
from gtts import gTTS
from streamlit_mic_recorder import mic_recorder
import io
import wave

st.title("AI Voice Assistant")

# -------- TEXT INPUT --------
text_input = st.text_input("Type your question")

# -------- VOICE INPUT --------
audio = mic_recorder(start_prompt="🎤 Start recording",
                     stop_prompt="⏹ Stop recording",
                     key='recorder')

voice_text = ""

if audio:

    # Convert audio bytes to proper WAV
    wav_bytes = io.BytesIO(audio['bytes'])

    with wave.open("voice.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(wav_bytes.read())

    r = sr.Recognizer()

    try:
        with sr.AudioFile("voice.wav") as source:
            audio_data = r.record(source)

        voice_text = r.recognize_google(audio_data)
        st.write("You said:", voice_text)

    except Exception as e:
        st.write("Voice recognition failed")

# -------- COMBINED INPUT --------
query = text_input if text_input else voice_text

if query:

    if "wikipedia" in query:
        topic = query.replace("wikipedia","")
        result = wikipedia.summary(topic, sentences=2)

    elif "hello" in query:
        result = "Hello, how can I help you?"

    else:
        result = "I could not understand"

    st.write(result)

    # Convert text to speech
    tts = gTTS(result)
    tts.save("answer.mp3")

    audio_file = open("answer.mp3","rb")
    st.audio(audio_file.read(), format="audio/mp3")
