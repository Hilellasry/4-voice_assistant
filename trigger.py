import speech_recognition as sr
from verbals import *
from do import *
import pyjokes
import time


def takeCommand():
    text = None 
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



start_time = time.time() #for the timer

def if_do(command):
    while True:
        current_time = time.time() #for the timer
        elapsed_time = current_time - start_time #for the timer
        
        
        
        #!------------------------------
        if "good morning" in command:
            say("maybe its a good morning... or maybe it's not")
       # if "4" or "four" or "for" in command:
       #  say("yes yes, you not need to say twice")  
       #  break 
        if "joke" in command:
            say(pyjokes.get_joke(language="en", category="neutral"))
        if "poopoo" in command:
            say("you poopoo, in your self")
        if "word" in command:
            say("words")
        if "word" in command:
            say("words")
        if "word" in command:
            say("words")
        
        #!-------------------------------
        
        
        
        if elapsed_time > listening_time:#break the loop 
            break 
    
