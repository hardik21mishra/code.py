import speech_recognition as sr
import os
import pyttsx3 #for windows specially to use say
import webbrowser
import openai

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise, please wait...")
            r.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
            r.pause_threshold = 1
            print("Listening...")
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Adjusting for ambient noise, please wait...")
#         r.adjust_for_ambient_noise(source)
#         # r.pause_threshold = 1 ##default 0.8
#         audio = r.listen(source)
#         try:
#             print("Recognising....")
#             query = r.recognize_google(audio, language = "hi-in")
#             print(f"User said: {query}")
#             return query
#         except Exception as e: 
#             return "Some Error Occured Sorry from Jarvis"

if __name__ == '__main__':
    print("vs code")
    say("Hello! I am your assistant")
    while True:
        print("Listening.......")
        query = takecommand()
        sites = [
    ["youtube", "https://youtube.com"], 
    ["google", "https://google.com"], 
    ["wikipedia", "https://en.wikipedia.org/wiki/Main_Page"], 
    ["twitter", "https://x.com"],
    ["facebook", "https://www.facebook.com"],
    ["instagram", "https://www.instagram.com"],
    ["linkedin", "https://www.linkedin.com"],
    ["reddit", "https://www.reddit.com"],
    ["amazon", "https://www.amazon.com"],
    ["netflix", "https://www.netflix.com"],
    ["spotify", "https://www.spotify.com"],
    ["github", "https://www.github.com"],
    ["pinterest", "https://www.pinterest.com"],
    ["yahoo", "https://www.yahoo.com"],
    ["bing", "https://www.bing.com"],
    ["cnn", "https://www.cnn.com"],
    ["bbc", "https://www.bbc.com"],
    ["hulu", "https://www.hulu.com"],
    ["ebay", "https://www.ebay.com"]
]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir....")
                webbrowser.open(f"{site[1]}")

        if "open chrome".lower() in query.lower():
            os.system(r'start "" "C:\Program Files\Google\Chrome\Application\chrome.exe"')

        say(query)