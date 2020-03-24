import speech_recognition as sr
import webbrowser as wb
import requests
from bs4 import BeautifulSoup

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening")
    audio = r.listen(source)

try:
    lyrics = r.recognize_google(audio, language='hi-IN')
    print("Searching for"+lyrics)
except Exception as e:
    print("Sorry! Can't hear you.")

if __name__ == '__main__':
    url = "https://open.spotify.com/search/" + lyrics
    wb.get().open(url)
