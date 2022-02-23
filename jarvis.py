import webbrowser

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty(voices,voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning!")
    elif hour >= 12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak ("I am Oomkar and Lara's Personal Siri, my name is Marshmellow, Please tell me, what would you like me to do ?")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")   #Say that again will be printed in case of improper voice
        return "None" #None string will be returned
    return query

if __name__=="__main__":
        speak("Lara and aku are good girls")
        wishme()
        while True:
            query=takeCommand().lower()

            if 'wikipedia' in query:
               speak('Searching Wikipedia...')
               query= query.replace("wikipedia","")
               results=wikipedia.summary(query,sentences=2)
               speak("According to Wikipedia")
               print(results)
               speak(results)
            elif 'open youtube' in query:

                webbrowser.open("youtube.com")

