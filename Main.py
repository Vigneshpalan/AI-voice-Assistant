from speak import speak
from listen import Mic
from brain import reply, Qreply
from Clap import Tester
import random
from open import Open
from wakeup import WakeupDetected

import json
import nltk
from nltk.stem.porter import PorterStemmer
import torch
from intent_prediction import predict_intent_response,load_model
# ... (Previous code)
import sys
def MainExc():
    speak("Hello sir, I am Jarvis.")
    while True:
        data = Mic()
        data = str(data).replace(".", "")

        if "stop" in data or "exit" in data:
            speak("Goodbye!")
            sys.exit(0)
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

def Clapdetect():
    q = Tester()
    if "True-Mic" in q:
        print("Clap detected")
        MainExc()
    else:
        pass

if __name__ =="__main__":
    if WakeupDetected():
        print("Wake-up phrase detected")
        Clapdetect()
    else:
        print("Wake-up phrase not detected")