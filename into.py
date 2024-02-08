#Translate in other language(speech to speech)   

import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
speech = pyttsx3.init()

# Initialize translator
translator = Translator()

print("Start talking")
with sr.Microphone() as source:
    audio = r.record(source , duration = 5)
    print("Recognizing...")
    try:
        # Use Google's speech recognition engine to transcribe speech to text
        text = r.recognize_google(audio)
        print("You said: " + text)
        
        translation = translator.translate(text, dest='en')
        print("Translation: " + translation.text)
        
        speech.say(translation.text)
        
        # Use Google Translate to translate the text to another language
        translation = translator.translate(text, dest='es')
        print("Translation: " + translation.text)
        
        speech.say(translation.text)
        # speech.runAndWait()
        
        translation = translator.translate(text, dest='fr')
        print("Translation: " + translation.text)
        
        # Use text-to-speech engine to convert the translated text to speech
        speech.say(translation.text)
        speech.runAndWait()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))