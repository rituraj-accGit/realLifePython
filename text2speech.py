#a python based app to convert text into speech

import pyttsx3

def soundmaker():

    givenText= input("provide text to be spoken: ")
    engine= pyttsx3.init()
    engine.say(givenText)
    engine.runAndWait()

soundmaker()