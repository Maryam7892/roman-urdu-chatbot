import streamlit as st
import requests
from gtts import gTTS
import uuid
import os
import base64

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

st.set_page_config(page_title="Roman Urdu Chatbot", layout="centered")
st.title("🗨️ Roman Urdu Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def get_bot_response(user_input):
    try:
        response = requests.post(RASA_URL, json={"sender": "user", "message": user_input})
        messages = response.json()
        bot_reply = "\n".join([msg["text"] for msg in messages if "text" in msg])
        return bot_reply if bot_reply else "Maaf kijiye, mujhe kuch samajh nahi aaya."
    except:
        return "Rasa server se response nahi mil raha."

def text_to_speech(text, lang="ur"):
    tts = gTTS(text=text, lang=lang)
    filename = f"tts_{uuid.uuid4()}.mp3"
    tts.save(filename)
    return filename

# User input
user_message = st.text_input("Aap ka sawal:", key="input")

if st.button("Send") and user_message.strip():
    st.session_state.chat_history.append(("You", user_message))
    bot_reply = get_bot_response(user_message)
    st.session_state.chat_history.append(("Bot", bot_reply))

# Chat + TTS
for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")
    if sender == "Bot" and msg.strip():
        audio_file = text_to_speech(msg)
        with open(audio_file, "rb") as audio:
            audio_bytes = audio.read()
        b64 = base64.b64encode(audio_bytes).decode()
        st.markdown(
            f"""
            <audio autoplay="true" controls>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True,
        )
        os.remove(audio_file)
