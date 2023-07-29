import os 
import keyboard
import pyautogui
import webbrowser
from listen import Listen
from speak import speak
from time import sleep
import datetime
def Open(q):
    application_mapping = {
        "vscode": "Visual Studio Code",
        "chrome": "Google Chrome",
        "cmd": "Command Prompt",
        "calculator": "Calculator",
        "notepad": "Notepad",
        "calendar": "Calendar",
        "email": "Email Client",
        "file_explorer": "File Explorer",
        "music_player": "Music Player",
        "video_player": "Video Player",
    }

    q=str(q).lower()
    if "search" in q:
        Link=f"http://www.{u}.com"
        webbrowser.open(Link)
        return True
    
    elif "time" in q:
        now = datetime.datetime.now()  # Use the full import path for datetime
        current_time_str = now.strftime("%H:%M:%S")  # Store the formatted time in a variable
        speak(current_time_str)
        return True

 
    elif "date"in q:
        current_date = datetime.date.today()
        formatted_date = current_date.strftime("%Y-%m-%d")
        speak(formatted_date)
        return True
    elif q in application_mapping:
        pyautogui.press("win")   
        sleep(1)
        keyboard.write(application_mapping[q])
        sleep(1)
        keyboard.press("enter")
        sleep(0.5)
        return True    

    return False