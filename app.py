import tkinter
from tkinter import *
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

root = tkinter.Tk()

userEntry = Entry(root, width=35, borderwidth=5)
userEntry.grid(row=0, column=0)

def speakEntry():
    speak(str(userEntry.get()))

speakButton = Button(root, text="Speak", command=speakEntry).grid(row=0, column=1)

root.mainloop()