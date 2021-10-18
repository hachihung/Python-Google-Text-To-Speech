import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="zh")
    filename = "voice.m4a"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="en")
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

speak("I am ready")
text = get_audio()

if "hello" in text:
    print("Hello, how are you?")
    speak("hello, how are you?")

if "name" in text:
    print("I am Python Siri!")
    speak("I am Python Siri!")

if "today" in text:
    print("Today is 18 Oct 2021.")
    speak("Today is 18 Oct 2021.")


# pip install SpeechRecognition
# pip install gTTS
# pip install playsound
# pip install pyaudio (will have problems)
# way out: download pyaudio https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
