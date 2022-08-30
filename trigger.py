import speech_recognition as sr
from verbals import *
from do import *

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        text = r.recognize_google(audio, language ='en-in')
        print(f"User said: {text}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return text




def if_do(command):
    if "good morning" in command:
        say("maybe its a good morning")
        
    