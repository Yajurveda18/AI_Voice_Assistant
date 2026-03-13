import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import pyttsx3
import wikipedia

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    fs = 44100
    seconds = 5

    print("Listening...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write("voice.wav", fs, recording)

    r = sr.Recognizer()
    with sr.AudioFile("voice.wav") as source:
        audio = r.record(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        print("Could not understand")
        return ""

while True:
    command = listen()

    if "wikipedia" in command:
        topic = command.replace("wikipedia", "")
        result = wikipedia.summary(topic, sentences=2)
        speak(result)

    elif "hello" in command:
        speak("Hello, how can I help you?")

    elif "exit" in command:
        speak("Goodbye")
        break
