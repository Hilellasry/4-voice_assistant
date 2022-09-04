import speech_recognition as sr
from trigger import  *
from do import *
#--------------------------------


while True:
    print(takeCommand())
    if name or nickname1 or nickname2 or nickname3 in takeCommand(): 
        print("yes?")
        if_do(takeCommand())
        
        
   
        
