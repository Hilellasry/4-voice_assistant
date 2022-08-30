import pyttsx3


def say(words):
    voicetype = 0  #!what voice is this (1 for male voice)(1 for female voice)
    
    eng = pyttsx3.init() #initialize an instance
    
    voice = eng.getProperty('voices') #get the available voices
    eng.setProperty('voice', voice[voicetype].id) #changing voice to index 1 for female voice
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
    
    
say("hi there")