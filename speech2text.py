#python application which understands speech and displays it as text

import speech_recognition as sr

def convertAudio():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something..!")
        audio= r.listen(source)
        print("done!")

    try:
        text= r.recognize_google(audio)
        print("you said "+ text)

    except Exception as e:
        print(e)

convertAudio()