import os
import time
import playsound
import speech_recognition as sr 
from gtts import gTTS

def speak(text):
    tts=gTTS(text=text,lang ="en")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source)
        audio =r.listen(source,timeout=5)
        
        said = "" 
        
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e :
            print("Exception : "+str(e))

    return said

# speak(" hai prends")
text= get_audio()

if "hello" in text :
    speak("hello how are you")

if "what is my name" in text:
    speak("your name is rajesh")
