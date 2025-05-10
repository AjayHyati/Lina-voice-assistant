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

📁 Project Structure
```
lina-voice-assistant/
│
├── lina.py           # Main script for the voice assistant
├── musiclib.py       # Dictionary of song names mapped to their URLs
├── README.md         # Project documentation
```


📝 Sample musiclib.py
```
music = {
    "hello": "https://www.youtube.com/watch?v=example1",
    "summer": "https://www.youtube.com/watch?v=example2",
    "blinding": "https://www.youtube.com/watch?v=example3"
}
```
You can add or update song names and links as needed.


🔑 Get Your NewsAPI Key

1.Go to https://newsapi.org/

2.Create an account and generate your API key.

3.Replace the placeholder key in lina.py:

```
newsapi = "your_api_key_here"
```
🚀 How to Run Lina

1.Clone the repository or download the files:
```
git clone https://github.com/yourusername/lina-voice-assistant.git
cd lina-voice-assistant
```

2.Install dependencies (see above).

3.Run the assistant:
```
python lina.py
```

4.Say "Lina" when prompted, then give one of these commands:

• open google

• open youtube

• open facebook

• open linkedin

• play hello (or any song in musiclib.py)

• news (reads current headlines)


💡 Tips for Better Performance
• Use a good microphone or headset for clearer voice input.

• Speak clearly after the "Listening..." prompt appears.

• Ensure you have a stable internet connection for API-based services.







 


