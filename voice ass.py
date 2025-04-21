import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime
import webbrowser
import os
from dotenv import load_dotenv

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Take voice input from user and return as text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

def greet():
    """Greet the user based on time of day"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am your voice assistant. How can I help you?")

def run_assistant():
    """Main function to run the voice assistant"""
    greet()
    while True:
        query = take_command().lower()
        
        if 'play' in query:
            song = query.replace('play', '')
            speak(f'Playing {song}')
            pywhatkit.playonyt(song)
            
        elif 'time' in query:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f'The current time is {current_time}')
            
        elif 'who is' in query or 'what is' in query:
            person = query.replace('who is', '').replace('what is', '')
            info = wikipedia.summary(person, sentences=2)
            speak(info)
            
        elif 'date' in query:
            today = datetime.date.today().strftime('%B %d, %Y')
            speak(f"Today's date is {today}")
            
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            
        elif 'search' in query:
            search_query = query.replace('search', '')
            speak(f'Searching for {search_query}')
            pywhatkit.search(search_query)
            
        elif 'open youtube' in query:
            webbrowser.open('https://youtube.com')
            
        elif 'open google' in query:
            webbrowser.open('https://google.com')
            
        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com')
            
        elif 'exit' in query or 'quit' in query or 'goodbye' in query:
            speak("Goodbye! Have a nice day.")
            break
            
        else:
            speak("I didn't understand that. Can you please repeat?")

if name == 'main':
    run_assistant()