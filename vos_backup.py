import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
from datetime import datetime
from system import system_commands

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(text):
    print("VOS:", text)
    engine.say(text)
    engine.runAndWait()


recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        command = command.lower()
        print("You said:", command)
        return command

    except:
        speak("Please say that again.")
        return ""


speak("Hello Uvann. V O S is ready.")

while True:

    command = listen()
while True:
    command = listen()


    if command == "":
        continue

    # Greeting
    if "hello" in command:
        speak("Hello Uvann. How are you today?")

    elif "how are you" in command:
        speak("I am absolutely fine. Thank you for asking.")

    elif "your name" in command:
        speak("My name is V O S. Your personal assistant.")

    # Google
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "search" in command and "google" in command:
        query = command.replace("search", "")
        query = query.replace("on google", "")
        webbrowser.open(
            "https://www.google.com/search?q=" + query.strip()
        )
        speak("Searching Google")
        # check system commands first
    if system_commands(command):
        continue
        

    # YouTube
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "youtube" in command:
        pywhatkit.playonyt(command)
        speak("Playing on YouTube")
    # ChatGPT
elif "open chatgpt" in command or "open chat g p t" in command or "chatgpt" in command:
        webbrowser.open("https://chatgpt.com")
    speak("Opening ChatGPT")
    
    # WhatsApp
    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp")

    # Time
    elif "time" in command:
        current = datetime.now().strftime("%I:%M %p")
        speak("Current time is " + current)

    # Date
    elif "date" in command:
        today = datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + today)

    # Exit
    elif "exit" in command or "stop" in command:
        speak("Goodbye Uvann.")
        break

    else:
        speak("Sorry. I don't understand that command.")