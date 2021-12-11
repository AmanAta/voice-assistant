import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voice[0].id)
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
    except BaseException as e:
        speak("say that again please...")
        return "none"
    return query


# for wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak(" hi sir , good morning! ")
    elif hour > 12 and hour < 18:
        speak(" hi sir , good afternoon! ")
    else:
        speak(" hi sir , good evening! ")
    speak(" please tell me how can i help you! ")


# for send email
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('officialwildesports@gmail.com', 'Mdamanata8@')
    server.sendmail('officialwildesports@gmail.com', to, content)
    server.close()


if __name__ == "__main__":

    wish()

    while True:
        # if 1:

        query = takecommand().lower()

        # logic building for task
        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open vs code" in query:
            npath = "C:\\Users\\mdama\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(npath)

        elif "open visual studio code" in query:
            npath = "C:\\Users\\mdama\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(npath)

        elif "open game" in query:
            npath = "C:\\Users\\mdama\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(npath)

        elif "open valorant" in query:
            npath = "C:\\Users\\mdama\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(npath)

        elif "open zoom" in query:
            npath = "C:\\Users\\mdama\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(npath)

        elif "open photoshop" in query:
            npath = "C:\\Program Files (x86)\\Photoshop\\Photoshop.exe"
            os.startfile(npath)

        elif "open adobe photoshop" in query:
            npath = "C:\\Program Files (x86)\\Photoshop\\Photoshop.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(5)
                if k == 4:
                    break;
            cap.release()
            cv2.destroyAllWindow()

        elif "play music" in query:
            music_dir = "D:\\Arzoo\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "play any music" in query:
            music_dir = "D:\\Arzoo\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "play some music" in query:
            music_dir = "D:\\Arzoo\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "play some songs" in query:
            music_dir = "D:\\Arzoo\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "play any song" in query:
            music_dir = "D:\\Arzoo\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))


        elif "wikipedia" in query:
            speak("searching wikipedia.......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia...")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open linkedin" in query:
            webbrowser.open("https://in.linkedin.com")

        elif "open blackboard" in query:
            webbrowser.open("https://cuchd.blackboard.com")

        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif "what is the time right now" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif "what is the time now" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "search on google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send a message to vishal" in query:
            kit.sendwhatmsg("+918808937015", "this message sending by assistant", 00, 46)

        elif "play songs on youtube" in query:
            kit.playonyt("beleiver")

        elif "play some music from youtube" in query:
            kit.playonyt("tum hi ho")

        elif "play beleiver song on youtube" in query:
            kit.playonyt("beleiver")

        elif "play old song on youtube" in query:
            kit.playonyt("ek pyar ka nagma hai")

        elif "play any song on youtube" in query:
            kit.playonyt("best romantic hindi songs")


        elif "send email to vishal" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "vishalps2606@gmail.com"
                sendEmail(to, content)
                speak("email has been sent to vishal")

            except Exception as e:
                print(e)
                speak("sorry sir , i am not able to sent")

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        elif "NO" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        elif "all done for now" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        speak("sir, do you have other work! ")
