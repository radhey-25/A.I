import pyttsx3  #pip install pyttsx3 - Text To Speech(tts)
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis...")

Sir = "DeBangshu Chanda" 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function will pronounce the string which is passed to it
def speak(text) : 
    engine.say(text)
    engine.runAndWait()


# This function will wish you as per the current time 
def wishMe() :
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12 :
        print("Very Good Morning!" +" "+ Sir)
        speak("Very Good Morning" + Sir)
        
    elif hour >= 12 and hour < 18 :
        print("Very Good Afternoon!" +" "+ Sir)
        speak("Very Good Afternoon" + Sir)
 
    else :
        print("Very Good Evening!" +" "+ Sir)
        speak("Very Good Evening" + Sir)

    print("I am Jarvis Sir! Please tell me how may I help you?")
    speak("I am Jarvis Sir. Please tell me how may i help you")

# This fuction will take command from the microphone
def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

        try :
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n")

        except Exception as e :
            # print(e)
            print("Say that again please...")
            return "None" 
        
        return query 

# This function will send email to Default Email
def sendEmail(to, content) :
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('debangshuchandra1999@gmail.com', 'Deba@1234')
    server.sendmail("adrikaroy8327@gmail.com", to, content)
    server.close

# Main Program starts here...
def main() :
    speak("Initializing Jarvis")
    wishMe()
    while True :
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query.lower() :
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        

        elif 'open youtube' in query.lower():
            webbrowser.open("youtube.com")
        
        elif 'open google' in query.lower():
            webbrowser.open("google.com")

        elif 'open Spotify' in query.lower():
            os.startfile("Spotify")
        
        elif 'open Microsoft Edge' in query.lower():
            os.startfile("Microsoft Edge")
        
        elif 'open My Sql Shell' in query.lower():
            os.startfile("My Sql Shell")
      
        elif 'open Facebook' in query.lower():
            os.startfile("Facebook")

        elif 'open File Explorer' in query.lower():
            os.startfile("File Explorer")
        

        elif 'open Intellij IDEA Community Edition 2022.1.1' in query.lower():
            os.startfile("Intellij IDEA Community Edition 2022.1.1")
        
        elif 'play music' in query.lower() :
            songs_dir = 'F:\\Music'
            songs = os.listdir(songs_dir)
            # print(songs)
            os.startfile(os.path.join(songs_dir, songs[15]))

        elif 'time' in query.lower() :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
            

        elif 'code' in query.lower() :
            codePath = "C:\\Users\\Debangshu Chanda\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Deba' in query.lower():
            try :
                speak("What should I send")
                content = takeCommand()
                to = "debangshuchandra27@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e :
                print(e)
                speak("Sorry Sir, currently i am not able to send this email")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()        


main()
