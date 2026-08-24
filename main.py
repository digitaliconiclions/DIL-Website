import pywhatkit
import os
import webbrowser

name = input("What is your name? ")
print(f"Welcome {name}")

command = input("What do you want me to do? ").lower()

if "youtube" in command:
    pywhatkit.playonyt(command)

elif "google" in command:
    webbrowser.open("https://www.google.com")

elif "calculator" in command:
    os.system("calc")

if "youtube" in command:
    pywhatkit.playonyt(command)

elif "google" in command:
    webbrowser.open("https://www.google.com")

elif "calculator" in command:
    os.system("calc")

elif "chatgpt" in command:
    webbrowser.open("https://chatgpt.com")

elif "search" in command:
    pywhatkit.search(command)

else:
    print("Sorry, I don't understand.")