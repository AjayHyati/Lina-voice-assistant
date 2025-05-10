# 🤖 Lina - A Voice-Controlled Virtual Assistant

Lina is a personal voice assistant built with Python that listens to your commands and performs tasks like opening websites, playing music, and reading out the latest news headlines. Just say "Lina" to activate it and give your command!

---

## 🎯 Project Purpose

The aim of Lina is to demonstrate how speech recognition and voice synthesis can be used to build a simple, interactive virtual assistant using Python. This assistant can:

- Recognize spoken keywords and commands
- Respond through speech using text-to-speech
- Perform useful actions like opening websites, playing songs, or reading the news

---

## 📌 Features

- **Wake Word Activation**: Say "Lina" to trigger the assistant.
- **Speech Recognition**: Converts spoken commands to text using Google's Speech API.
- **Text-to-Speech**: Speaks responses using `pyttsx3`.
- **Web Automation**: Opens frequently used websites like:
  - Google
  - Facebook
  - YouTube
  - LinkedIn
- **Play Music**: Plays a song from a predefined dictionary (`musiclib.py`).
- **Read News**: Fetches top US news headlines from NewsAPI and reads them aloud.

---

## 🧰 Requirements

Install the following Python packages:

```
pip install SpeechRecognition pyttsx3 requests
```
For microphone input, also install:
```
pip install pyaudio
```
⚠️ Note: On Windows, you may need to install PyAudio from a .whl file if installation via pip fails. You can find suitable wheels at https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio




 


