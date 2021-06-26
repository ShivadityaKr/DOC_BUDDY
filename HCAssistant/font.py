import tkinter as tk
from tkinter import *
import datetime

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

root = tk.Tk()
root.geometry('1300x1300+0+0')
root.title('DOC-BUDDY')
from PIL import ImageTk, Image

root.configure(bg="white")
img = ImageTk.PhotoImage(file="img.jpg")

Label(root, image=img).place(x=570, y=130, height=200, width=200)


def doc():
    listener = sr.Recognizer()
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def talk(text):
        engine.say(text)
        engine.runAndWait()


    def take_command():
        try:
            with sr.Microphone() as source:
                print("Listening...")
                listener.adjust_for_ambient_noise(source, duration=0.2)
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'doctor' in command:
                    command = command.replace('doctor', '')
                    print(command)
        except:
            pass
        return command

    def run_doctr():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Curren time is' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'how to overcome' in command:
            info = pywhatkit.info(command)
            talk(info)
        elif 'tell me about' in command:
            info = pywhatkit.info(command)
            talk(info)
        elif 'what is' in command:
            info = pywhatkit.info(command)
            talk(info)
        elif 'headache' in command:
            talk("drinking a warm cup of tea may provide some relief from the throbbing, distracting pain in your head")
        elif 'stomach' in command:
            talk(
                "A simple remedy is to place a heating pad where it hurts on your stomach. The heat relaxes your outer stomach muscles and promotes movement in the digestive tract. Lying down usually works best.")
        elif 'body pain' in command:
            talk(
                "Massaging your body with warm mustard oil can help relieve pain. Research shows that mustard oil contains a compound called allyl isothiocyanate which reduces inflammation in the body")
        elif 'fever' in command:
            talk("")
        elif '' in command:
            talk("please say again")

        else:
            talk('please say again')

    while True:
        run_doctr()






# def new():
#     flag = load()
#     if flag == 1:
#         print("yes")
#         doc()


def bttn(x, y, text, ecolor, lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor  # ffcc66
        myButton1['foreground'] = lcolor  # 000d33

    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground'] = ecolor

    myButton1 = Button(root, text=text,
                       width=20,
                       height=5,
                       fg=ecolor,
                       border=0,
                       bg=lcolor,
                       activeforeground=lcolor,
                       activebackground=ecolor,
                       command=lambda : doc()
                       )

    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x, y=y)


bttn(600, 330, 'S T A R T', '#8cd3f5', '#000000')
Label(root, text="// Click on START Button to activate...", font="comicsense 10 italic", fg="#9da1a8", bg="white").place(x=600, y=420)
Label(root, text="// Say Doctor and then your query...", font="comicsense 10 italic", fg="#9da1a8", bg="white").place(x=600, y=440)
Label(root, text="// like.. Hey Doctor I have headache", font="comicsense 10 italic", fg="#9da1a8", bg="white").place(x=600, y=460)
root.mainloop()
