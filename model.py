import datetime
import wikipedia

def process_command(command, speak):

    if "hello" in command:
        speak("Hello, how can I help you")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + time)

    elif "wikipedia" in command:
        speak("Searching Wikipedia")
        result = wikipedia.summary(command, sentences=2)
        speak(result)

    elif "your name" in command:
        speak("I am your AI voice assistant")

    else:
        speak("Sorry, I do not know the answer")