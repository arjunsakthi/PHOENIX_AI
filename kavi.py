# from cmd import PROMPT
from PIL import Image,ImageTk # pip install pillow
import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as pr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import time
import webbrowser as wb # pip install webbrowser
from playsound import playsound # pip install playsound
import os
import random
import openai # pip install openai
from logo3 import *
from email.message import EmailMessage
import ssl
import smtplib
import pywhatkit # pip install pywhatkit




openai.api_key ="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"

engine = pyttsx3.init()
rate = engine.getProperty('rate')                         
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

size = (300,300)



def speak(prad):
    engine.say(prad)
    engine.runAndWait()

#speak(response)

def sime():
    speak("the current time is ")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = datetime.datetime.now().month
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)

def wishgood():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning ")
    elif hour >=12 and hour<18:
        speak("Good Afternoon ")
    elif hour >=18 and hour<21:
        speak("Good Evening ")
    elif hour >=21:
        speak("Good night ")

def wishwelcome():
    speak("!!welcome back sir!!")
    sime()
    date()
    speak("Phoenix at your service . please tell me how can i help you")


def takeCommand():
    
    r = pr.Recognizer()  # initalising the recogniser
    with pr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 # wait for one second and then listen the audio
        r.adjust_for_ambient_noise(source) # adjust the microphone for ambient noise reduction
        audio = r.listen(source) # source nothing but listening our microphone
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') # Recognize our voice
        # Requires an internet connection
        print(query)
    

    except Exception as e:
        print(e)
        speak("Say that thing again please...")
        return 'None'
    return query

def whatsup():
    
    # For working : Need to sign to your whatsup in current pc

    try:
    
        speak("Type the Recievers phone number")
        reciver_number=input("Enter the Recievers phone number : ")
        speak("Type message to be delivered")
        message=input("Type the Message to be delivered : ") 
        pywhatkit.sendwhatmsg("+91"+reciver_number,
                                message,
                                datetime.datetime.now().hour, datetime.datetime.now().minute+1)
        print("Successfully Sent!")
    
    except:
    
        print("An Unexpected Error!")


def email():
    em=EmailMessage()
    speak("Type sender's mail id.")
    email_sender=input("Type sender's mail id : ")
    speak("Type reciever's mail id.")
    email_receiver=input("Type reciever's mail id : ")
    speak("Type sender email password")
    speak("Given below is the link to acces your gmail app password")
    print("https://myaccount.google.com/u/4/apppasswords")
    email_password=input("Type sender gmail app password : ")
    speak("Type the subject of the mail")
    subject=input("Type the subject of the Mail : ")
    speak("Type the body of the mail")
    body=input("Type the body of the Mail : ")
    em['From']=email_sender
    em['To']=email_receiver
    em['subject']=subject
    em.set_content('''%s'''%body)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

def self_destruct():
    speak("salf destructing the laptop sir")
    speak("starting the countdown")
    speak("5")
    speak("4")
    speak("3")
    speak("2")
    speak("1")
    playsound("./Explosion.mp3")
  #  sound_file = vlc.MediaPlayer("./Explosion+3.mp3")
   # sound_file.play()
    #time.sleep(5)
    speak("sorry sir your laptop has just got destroyed sir")
def shoot():
    w = query.split()
    a = w[-1]
    speak("guns are turned over to"+a)

    speak("shooting order getting initialise sir")
    speak("count down for shotting started sir")
    speak("3")
    speak("2")
    speak("1")
    playsound("./gun_shoot.mp3")
  #  sound_file1 = vlc.MediaPlayer("./gun_shoot.mp3")
   # sound_file1.play()
    time.sleep(8)

#need to loop it out for 3 times if name is not recogonised

def infinty():
    model_engine = "text-davinci-003"
    print('enter what do you want to ask to me')
    speak('enter what do you want to ask to me')
    prompt = takeCommand().lower()

    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5,
    )

    # Print the response
    response= completion.choices[0].text
    print(response)
    speak(response)
    print('do you want to ask more questions to me ? \nif yes then please say one more otherwise say exit')
    speak('do you want to ask more questions to me ?\nif yes then please say one more otherwise say exit')

def music():
    music_dir = 'E:\pyttsx3_jarvis\music'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,random.choice(songs)))

speak("can i know your name")
ask = takeCommand()
c=0
while(c!=3):
    c=c+1
    if (ask=='None'):
        ask = takeCommand()
    else:
        break
    print(ask)
    

if __name__ == "__main__":
    wishgood()
    if (ask == 'None'):
        speak("Welcome Boss") 
        speak("Pheonix at your service . please tell me how can i help you")

    else:
        speak("Welcome"+ask+"boss")
        speak("Pheonix at your service . please tell me how can i help you")

    while True:
        query=takeCommand().lower()
        if 'time' in query:
            sime()
        elif 'date' in query:
            date()
        elif 'offline' in query:
            speak('ok sir bye, see u later sir')
            
            break
        
        elif 'open infinity' in query:
            speak("opening!")
            #9infinty()
            speak('say GO to KICKstart your Infinity experience')
            print('say GO to KICKSTART your INFINITY experience')
            while 1:
                if(takeCommand().lower()!= 'exit'):
                    infinty()
                    
                else:
                    speak("THANK YOU PLEASE DO VISIT INFINITY SECTION OF PHEONIX AGAIN")
                    break
        elif 'mail' in query:
            email()
        elif 'whatsup' in query:
            whatsup()   
        elif 'whatsapp' in query:
            whatsup()   
        elif 'goodbye' in query:
            speak('ok sir bye see u later sir')
            break
        elif 'play music'in query:
            print('playing a random song sir!')
            speak('playing a random song sir!')
            music()
        elif 'more about you' in query:
            speak("my name is pheonix ,having 12th Gen Intel(R) Core(TM) i9-12900K @ 5.2Giga Hertz and Windows 11 pro os with 64 bit operating system and 64.0 giga bite ram with nvidia Geforce RTX 6gb GDDr5 graphics card ,this is all in my creators system ,i live in there")
        elif "creators name" in query:
            speak("my developers names are Mr.K.Sakthivel,Mr.Athul Krishna.K.R,Mr.Vamsi Krishna,Mr.Ankit")
            out = Image.open('./image/sak.jpg')
            out.size
            out.show()
        elif "creator's name" in query:
            speak("my developers names are Mr.K.Sakthivel,Mr.Athul Krishna.K.R,Mr.Vamsi Krishna,Mr.Ankit")
            out = Image.open('./image/sak.jpg')
            out.size
            out.show()
        elif "more about about your " in query:
            speak("They are group of genius ,who gave me a life in this earth . They all are my family members ,who have all knowledge about me .They are master in programming , who have programmed me ,so well nice.iam saying that , They will real gonna success in their life , for their hardwork")
        elif "it's ok" in query:
            speak("it's my duty sir")
        
        elif 'make a note' in query:
            speak("what should I note?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('sak.txt','w')
            remember.write(data)
            remember.close()
        elif 'read the note' in query:
            remember = open('sak.txt','r')
            speak("you said me to remember that"+remember.read())
            
        elif 'wikipedia' in query:
            while True:
                try:
                    speak("What to do you want to search ?")
                    query=takeCommand().lower()
                    speak("searching")
                    speak("few lines or a para")
                    s = takeCommand()
                    if 'few lines' in s:
                        result = wikipedia.summary(query, sentences=2 )
                    elif 'para' in s:
                        result = wikipedia.summary(query, sentences=5 )
                    print(result)
                    speak(result)
                    break
                except:
                    speak("can't find that thing sir")
        elif 'search in chrome' in query:
            speak("what should i search ?")
            command = takeCommand().lower()
            wb.open('https://google.com/search?q='+command)
        elif 'self' in query:
            self_destruct()
            break
        elif 'hi' in query:
            speak("hello")
        elif 'hello' in query:
            speak("hi"+ask)
            speak("how are you?")
            speak("i hope you are fine")
        elif 'hey' in query:
            speak("hi"+ask)
            speak("how are you?")
            speak("i hope you are fine")
        elif 'thank' in query:
            speak("no problem ,it's my duty")
        elif 'thanks' in query:
            speak("no problem ,it's my duty")
        elif 'yes' in query:
            speak("good")
        elif 'nice' in query:
            speak("very nice")
        elif 'shoot' in query:
            shoot()
        else :
            speak("Command not Recogonised")
            print("Command not Recogonised")


        
