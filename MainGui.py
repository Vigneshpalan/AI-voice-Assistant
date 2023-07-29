import tkinter as tk
from speak import speak
from intent_prediction import predict_intent_response, load_model
import threading
from speak import speak
from listen import Mic
from brain import reply, Qreply
from Clap import Tester
import random
from open import Open
from wakeup import WakeupDetected

import time

def speak_response(text):
    speak(text)
    response_label.config(text="JARVIS: " + text)

def process_command():
    command = command_entry.get().strip()
    command_entry.delete(0, tk.END)

    if command:
        tag, responses = predict_intent_response(command)
        tag_list = ["greet", "goodbye", "fallback", "about","help","thanks"]
        if any(tag in tag_list for tag in tag):
                speak(random.choice(responses))
                if "goodbye" in tag :
                     speak("Goodbye!")
                     SystemExit

                
        else:
                speak(random.choice(responses))
                Open(tag)
                
def on_enter_pressed(event):
    process_command()

def start_jarvis():
    speak("Hello sir, I am Jarvis.")
    while True:
        data = Mic() # Replace this with your audio input mechanism
        data = str(data).replace(".", "")

        if "stop" in data or "exit" in data:
            speak("Goodbye!")
            break
        elif len(data) <= 3:
            pass
        elif "what is" in data or "where" in data or "question" in data or "answer" in data:
            speak(Qreply(data))
        else:
            # Use intent prediction function from intent_prediction.py to get a response
            tag, responses = predict_intent_response(data)
            tag_list = ["greet", "goodbye", "fallback", "about","help","thanks"]
            if any(tag in tag_list for tag in tag):
                speak(random.choice(responses))
            else:
                speak(random.choice(responses))
                Open(tag)

def start_voice_assistant():
    voice_button.config(state=tk.DISABLED)
    command_entry.delete(0, tk.END)
    command_entry.focus()

    # Start JARVIS in a separate thread to keep the GUI responsive
    jarvis_thread = threading.Thread(target=start_jarvis)
    jarvis_thread.start()

    # After processing, enable the voice_button again
    # The following loop waits for the JARVIS thread to finish
    while jarvis_thread.is_alive():
        time.sleep(0.1)
    
    voice_button.config(state=tk.NORMAL)

app = tk.Tk()
app.title("JARVIS GUI")
app.geometry("400x300")

command_entry = tk.Entry(app, width=50)
command_entry.pack(pady=10)
command_entry.bind("<Return>", on_enter_pressed)

submit_button = tk.Button(app, text="Submit", command=process_command)
submit_button.pack()

response_label = tk.Label(app, text="JARVIS: Hello, I am ready. Please give me a command.", wraplength=380, justify="left")
response_label.pack(pady=20)

voice_button = tk.Button(app, text="Voice Assistant", command=start_voice_assistant)
voice_button.pack()

if __name__ == "__main__":
    app.mainloop()
