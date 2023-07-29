import speech_recognition as sr
from googletrans import Translator
import sys
import keyboard
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Press Enter to start listening...")
        keyboard.wait("enter")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 10)
    try:
        print("Recognizing...")
        q = r.recognize_google(audio)
        q = q.lower()
        if "exit" in q:
            print("Goodbye!")
            
            return None
        return q
    except:
        return ""

def Trans(text):
    t = Translator()
    result = t.translate(text, dest='en')
    data = result.text
    print(f"YOU: {data}.")
    return data

def Mic():
  while True:
        q = Listen()
        if q:
            data = Trans(q)
            if "exit" in data:
                print("Goodbye!")
                sys.exit(0)
            else:
                return data

if __name__ == "__main__":
    while True:
        result = Mic()
        if result is None:
            break
