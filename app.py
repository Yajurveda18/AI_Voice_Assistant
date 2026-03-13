import speech_recognition as sr
import pyttsx3
from model import process_command

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        print("Could not understand")
        return ""

def main():
    speak("Voice assistant started")

    while True:
        command = listen()

        if command == "":
            continue

        if "exit" in command:
            speak("Goodbye")
            break

        process_command(command, speak)

if __name__ == "__main__":
    main()