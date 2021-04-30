import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

def run_sam():
    text = get_audio()

    if "hello" in text:
        speak("hello, how are you?")
    elif "what's your name" in text:
        speak("My name is sam")
    elif "do you love me" in text:
        speak("No, because you are ugly.")
    else:
        speak("talk normal i cant understand you")

run_sam()
