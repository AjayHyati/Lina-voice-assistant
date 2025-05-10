import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclib
import requests

recognizer=sr.Recognizer()
engine=pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait() 

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")   
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")   
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")   
    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkdin.com")   
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclib.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r= requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=d014042e68ae4029b4150b700ec79f03")
        if r.status_code == 200:

            #parse the json response
            data=r.json()

            #Extract the articles
            articles=data.get("articles",[])

            #speak the headlines
            for article in articles:
                speak(article["title"])
    



    
if __name__ =="__main__":
    speak("hiiii sir how may i help you")
    #obtain audio from the microphone
    while True:
        r = sr.Recognizer()
        print("Recognising......")
            

        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if (word.lower()== "Lina"):
                speak("Yes")

                with sr.Microphone() as source:
                    print("Lina activated")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    process_command(command)


            
        except Exception as e:
            print("Sphinx error; {0}".format(e))
