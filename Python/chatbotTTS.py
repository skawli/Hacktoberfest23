import random
import nltk
import speech_recognition as sr
from nltk.chat.util import Chat, reflections
from gtts import gTTS
import os

# Define patterns and responses for the chatbot
chatbot_responses = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ["I'm just a computer program, but I'm doing well. How about you?", "I don't have feelings, but thanks for asking!"]),
    (r'what is your name', ["I'm just a chatbot, so I don't have a name. You can call me ChatGPT.", "I'm your friendly neighborhood chatbot!"]),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Farewell!']),
    (r'(.*)', ["I'm not sure I understand. Could you please rephrase that?", "Can you tell me more about that?"]),
]

# Create a chatbot
chatbot = Chat(chatbot_responses, reflections)

# Initialize the speech recognition recognizer
recognizer = sr.Recognizer()

def listen_for_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        print("Audio captured.")
    return audio

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

def main():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")

    while True:
        user_input = input("You (text or say 'voice'): ").strip().lower()

        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
        elif user_input == 'voice':
            audio = listen_for_audio()
            try:
                user_input = recognizer.recognize_google(audio)
                print("You (voice):", user_input)
            except sr.UnknownValueError:
                print("Sorry, I could not understand your audio.")
                continue
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                continue

        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        text_to_speech(response)

if __name__ == "__main__":
    main()
