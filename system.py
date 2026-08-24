import os
import webbrowser
import subprocess

def system_commands(command):

    command = command.lower()

    # Calculator
    if "open calculator" in command:
        os.system("calc")
        return True

    # Notepad
    elif "open notepad" in command:
        os.system("notepad")
        return True

    # Paint
    elif "open paint" in command:
        os.system("mspaint")
        return True

    # Camera
    elif "open camera" in command:
        os.system("start microsoft.windows.camera:")
        return True

    # Command Prompt
    elif "open cmd" in command or "open command prompt" in command:
        os.system("start cmd")
        return True

    # VS Code
    elif "open visual studio code" in command or "open vs code" in command:
        os.system("code")
        return True

    # File Explorer
    elif "open file explorer" in command:
        os.system("explorer")
        return True

    # Downloads
    elif "open downloads" in command:
        os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))
        return True

    # Documents
    elif "open documents" in command:
        os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))
        return True

    # Desktop
    elif "open desktop" in command:
        os.startfile(os.path.join(os.path.expanduser("~"), "Desktop"))
        return True

    # Gmail
    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        return True

    # Facebook
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        return True

    # Instagram
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
        return True

    # LinkedIn
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        return True

    # Twitter/X
    elif "open twitter" in command or "open x" in command:
        webbrowser.open("https://x.com")
        return True

    return False 