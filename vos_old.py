import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import datetime

engine = pyttsx3.init()

def speak(text):
    print("VOS:", text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("Hello Uvann. VOS is ready.")

while True:
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        command = r.recognize_google(audio).lower()

        print("You said:", command)

        if "youtube" in command:
            speak("Opening YouTube")
            song = command.replace("youtube", "").replace("play", "").strip()

            if song == "":
                webbrowser.open("https://www.youtube.com")
            else:
                pywhatkit.playonyt(song)

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "chatgpt" in command:
            speak("Opening ChatGPT")
            webbrowser.open("https://chat.openai.com")

        elif "whatsapp" in command:
            speak("Opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The time is " + current_time)

        elif "date" in command:
            today = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + today)

        elif "exit" in command or "stop" in command:
            speak("Goodbye Uvann")
            break

        else:
            speak("Sorry, I don't understand.")

    except Exception:
        speak("Please say that again.")
import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import datetime

# ----------------------------
# Text To Speech Engine
# ----------------------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("VOS:", text)
    engine.say(text)
    engine.runAndWait()

# ----------------------------
# Speech Recognizer
# ----------------------------
r = sr.Recognizer()

speak("Hello Uvann. VOS is ready.")

while True:
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        command = r.recognize_google(audio)
        command = command.lower().strip()

        print("You said:", command)

        # ----------------------------
        # YouTube
        # ----------------------------
        if "youtube" in command:

            song = command.replace("open", "")
            song = song.replace("play", "")
            song = song.replace("youtube", "")
            song = song.strip()

            if song == "":
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
            else:
                speak("Playing " + song)
                pywhatkit.playonyt(song)

        # ----------------------------
# Google Search
# ----------------------------
elif "search" in command and "google" in command:

    search = command.replace("search", "")
    search = search.replace("on google", "")
    search = search.replace("google", "")
    search = search.strip()

    speak("Searching " + search)
    pywhatkit.search(search)

# ----------------------------
# Open Google
# ----------------------------
elif "open google" in command or command == "google":
    speak("Opening Google")
    webbrowser.open("https://www.google.com")
        # ----------------------------
        # ChatGPT
        # ----------------------------
        elif (
            "chatgpt" in command
            or "chat gpt" in command
            or "chat g p t" in command
            or "open chat" in command
            or "chat" in command
        ):
            speak("Opening ChatGPT")
            webbrowser.open("https://chatgpt.com")

        # ----------------------------
        # WhatsApp
        # ----------------------------
        elif "whatsapp" in command or "whats app" in command:
            speak("Opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com")

        # ----------------------------
        # Time
        # ----------------------------
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The time is " + current_time)

        # ----------------------------
        # Date
        # ----------------------------
        elif "date" in command:
            today = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + today)

        # ----------------------------
        # Exit
        # ----------------------------
        elif "exit" in command or "stop" in command:
            speak("Goodbye Uvann")
            break

        # ----------------------------
        # Unknown Command
        # ----------------------------
        else:
            speak("Sorry, I don't understand.")

    except Exception:
        speak("Please say that again.")