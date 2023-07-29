import pyttsx3
def speak(text):
    eng=pyttsx3.init("sapi5")
    voices=eng.getProperty("voices")
    eng.setProperty('voices',voices)
    eng.setProperty("rate",170)
    eng.runAndWait()
    print("")
    print(f'Jarvis :{text}.')
    eng.say(text)
    eng.runAndWait()

