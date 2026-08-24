import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("VOS:", text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    speak("I am listening")
    audio = r.listen(source)

try:
    command = r.recognize_google(audio)
    print("You said:", command)
    speak("You said " + command)

except:
    speak("Sorry, I could not understand")
if "youtube" in command.lower():
    pywhatkit.playonyt(command)

elif "google" in command.lower():
    webbrowser.open("https://www.google.com")

elif "chatgpt" in command.lower():
    webbrowser.open("https://chat.openai.com")

elif "whatsapp" in command.lower():
    webbrowser.open("https://web.whatsapp.com")

else:
    speak("Sorry, I don't understand.")
    