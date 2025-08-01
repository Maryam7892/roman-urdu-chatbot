import speech_recognition as sr
from gtts import gTTS
import requests
import uuid
import os
import time
import pygame

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

# Speak function with error check
def speak(text, lang="ur"):
    if not text or not text.strip():
        print("No text to speak.")
        return

    print(f"Bot: {text}")
    try:
        tts = gTTS(text=text, lang=lang)
        filename = f"response_{uuid.uuid4()}.mp3"
        tts.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.3)

        pygame.mixer.quit()
        os.remove(filename)
    except Exception as e:
        print(f"Error in TTS playback: {e}")

# Listen with microphone and STT
def listen(lang="ur-PK"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("You: (boliye)", end=" ", flush=True)
        try:
            audio = recognizer.listen(source, phrase_time_limit=10)
        except Exception as e:
            print(f"Microphone error: {e}")
            speak("Microphone ka masla hai.")
            return None

    try:
        text = recognizer.recognize_google(audio, language=lang)
        print(f"Transcribed Input: {text}")
        return text
    except sr.UnknownValueError:
        speak("Maaf kijiye, mein samajh nahi paaya.")
        return None
    except sr.RequestError:
        speak("Google Speech Service available nahi hai.")
        return None

# Chat loop
def chat():
    print("Voice Chat Mode (Say '/stop' to exit)\n")
    while True:
        user_input = listen()
        if not user_input:
            continue
        if user_input.lower() in ["stop", "/stop"]:
            speak("Allah Hafiz!")
            break

        try:
            response = requests.post(RASA_URL, json={"sender": "user", "message": user_input})
            bot_messages = response.json()
            if not bot_messages:
                speak("Bot se jawab nahi mila.")
                continue

            for msg in bot_messages:
                if "text" in msg and msg["text"].strip():
                    speak(msg["text"])
        except Exception as e:
            print(f"Error connecting to Rasa: {e}")
            speak("Bot se raabta nahi ho saka.")

if __name__ == "__main__":
    chat()