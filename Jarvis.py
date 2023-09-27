import speech_recognition as sr 
import pyttsx3   
import pywhatkit 
import datetime  
import wikipedia 
import pyjokes 
import webbrowser
import time
import keyboard 
from datetime import datetime 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def take_command():
    with sr.Microphone() as source:
        print('listening...')   
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower() 
    return command

def talk(text):
    engine.say(text)
    engine.runAndWait()


def run_Jarvis():
    command = take_command()
    print(command)
    if 'introduce' in command:
            talk(" Hey Everyone , This is JARVIS , Smart Voice Assistant , Build by CHIPSET team using Python . JARVIS Stands for Just A Really Very Intelligent System " )    
    
    elif 'telegram' in command:
        talk('opening telegram')
        webbrowser.open("https://webk.telegram.org/")
    
    elif 'spotify' in command:
        talk('opening spotify')
        webbrowser.open("https://open.spotify.com/")

    elif 'time' in command:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        talk(current_time)
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

#############################################################

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    
    elif 'google meet' in command:
        talk('enter meeting code')
        code = input("Enter meeting code: ")
        talk('opening google meet..')
        webbrowser.open(f"https://meet.google.com/{code}")
        time.sleep(3)
        keyboard.press_and_release('ctrl+e, space')
        time.sleep(1)
        keyboard.press_and_release('ctrl+d, space')
        time.sleep(1)
        talk('click ask to join..')
        talk('thank you')
    
    elif 'alarm' in command:
        talk('Please enter the time')
        Time=input("Enter the time (HH24:MM): ")
        while True:
            now = datetime.now()
            Standard_time= datetime.now().strftime("%H:%M")
            time.sleep(1)
            if Time==Standard_time:
                count=0
                while count<=2:
                    count=count+1
                    engine=pyttsx3.init()
                    engine.say("Times up")
                    engine.runAndWait()
                print("Thankyou For using the Interface")
                break

#################################################################

    elif 'exit' in command:
        talk("Thanks for giving me your time")
        exit()
    
    else:
        talk('Please say the command again.')

while True:
    run_Jarvis()