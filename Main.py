import speech_recognition as sr
from trigger import *
from do import *


while True:
    takeCommand()
    if "4" or "four" or "for" in takeCommand(): 
        takeCommand()
        if_do(takeCommand())
        
        
   
        
