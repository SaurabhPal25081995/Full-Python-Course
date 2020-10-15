# Read any text

# Method 1 by pyttsx3
import pyttsx3

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

# say method on the engine that passing input text to be spoken
engine.say('Hello sir, how may I help you, sir.')

# run and wait method, it processes the voice commands.
engine.runAndWait()

# Method 2 by gtts
from gtts import gTTS
import os

text = "Johny, Johny, yes papa Eating sugar? No, papa Telling lies? No, papa Open your mouth, hahaha!"

language = 'en'
speech = gTTS(text = text, lang = language, slow = False)
speech.save("poem.mp3")
os.system("start text.mp3")

