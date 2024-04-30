import speech_recognition as sr
import time
import pygame
import os

# Create a recognizer instance
r = sr.Recognizer()

# Define the activation word
activation_word = "jarvis"

# Define the sound file and volume
activation_sound = os.path.join("sounds","activation_sound.wav")
affermative_sound = os.path.join("sounds","affermative.wav")
volume = 0.5  # Volume should be between 0.0 and 1.0

# Initialize pygame mixer
pygame.mixer.init()

# Load the sound file

# Set the volume
pygame.mixer.music.set_volume(volume)

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")
    while True:  # The program will keep listening until it's stopped
        try:
            # Listen for the first phrase and extract it into audio data
            audio = r.record(source, duration=1.5)  # Listen for 2 seconds
            # Recognize speech using Google Speech Recognition
            text = r.recognize_google(audio, language='it-IT')
            if text.lower() == activation_word:
                print("Activation word detected. Listening ...")

                pygame.mixer.music.load(activation_sound)
                pygame.mixer.music.play()

                audio = r.record(source, duration=2.5 )  # Listen for 4 seconds
                print("Elaborating...")

                text = r.recognize_google(audio, language='it-IT')
                print("You said: " + text)
                
                pygame.mixer.music.load(affermative_sound)
                pygame.mixer.music.play()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        time.sleep(0.1)  # Short pause before next listen