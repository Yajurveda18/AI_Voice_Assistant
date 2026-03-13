import speech_recognition as sr
import pyttsx3
import wikipedia

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
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
