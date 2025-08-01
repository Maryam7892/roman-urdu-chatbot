# 🗣️ Roman Urdu Chatbot

A simple yet powerful **Roman Urdu chatbot** built using **Rasa** for natural language understanding and **Streamlit** for the user interface. The chatbot can reply in Roman Urdu and uses **gTTS (Google Text-to-Speech)** to respond with audio playback.

## 🌐 Live Demo

🔗 [Click here to try the chatbot](https://roman-urdu-chatbot.streamlit.app/)

---

## 🚀 Features

- 💬 Chat with the bot in Roman Urdu
- 🔊 Bot replies using TTS (Text-to-Speech)
- 🧠 Powered by Rasa NLU for intent classification and dialogue management
- 🎛️ Streamlit frontend for an easy-to-use web interface
- 🧪 Runs fully on free tools (Streamlit Community + local/remote Rasa server)

---

## 📂 Folder Structure

```
roman-urdu-chatbot/
├── app.py               # Streamlit frontend app
├── requirements.txt     # Dependencies for Streamlit Cloud
├── domain.yml           # Rasa domain file
├── data/
│   ├── nlu.yml          # Training examples
│   ├── rules.yml        # Rules for rule-based dialogue
│   └── stories.yml      # Stories for dialogue examples
├── actions/
│   └── actions.py       # Custom Rasa actions
├── config.yml           # Rasa pipeline and policies
├── endpoints.yml        # Rasa endpoints config
├── credentials.yml      # Channel config
└── README.md            # Project documentation
```

---

## 🧑‍💻 Technologies Used

- [Rasa](https://rasa.com/) – Conversational AI framework
- [Streamlit](https://streamlit.io/) – Python web app framework
- [gTTS](https://pypi.org/project/gTTS/) – Google Text-to-Speech
- [Python](https://www.python.org/) – Language of choice

---

## ⚙️ Setup Instructions

### 🖥️ Local Development

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/roman-urdu-chatbot.git
   cd roman-urdu-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Rasa server**
   ```bash
   rasa run --enable-api
   ```

4. **Start Streamlit app**
   ```bash
   streamlit run app.py
   ```

### ☁️ Deploy on Streamlit Cloud

1. Push the following files to a public GitHub repo:
   - `app.py`
   - `requirements.txt`
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"New app"**, select your repo and `app.py` as the main file
4. Deploy!

---

## 🔈 How It Works

- User types input in Roman Urdu
- The input is sent to the Rasa backend via REST API
- Rasa returns a Roman Urdu response
- The bot speaks the response using `gTTS` and plays it in the browser

---

## 📌 Sample Queries

```
tum kon ho?
abhi time kya hua hai?
mujhe joke sunao
tumhara naam kya hai?
```

---

## 🤖 Future Improvements

- Add **STT (Speech-to-Text)** for full voice interaction
- Improve intent classification with more examples
- Add fallback mechanism and sentiment understanding
- Host Rasa backend on cloud for 24/7 availability


---

## ✨ Credits

Developed with ❤️ using Rasa and Streamlit  
Maintained by **[Maryam](https://github.com/Maryam7892)**