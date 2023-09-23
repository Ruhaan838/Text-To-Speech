from gtts import gTTS
import os
from tkinter import *


def speech_to_text():
    language = 'en'
    text3 = text2.get()
    myobj = gTTS(text=text3, lang=language, slow=False)
    myobj.save("texttospeech.mp3")


def Open():
    os.system("texttospeech.mp3")


Box = Tk()
Box.geometry("400x200")

text1 = Label(Box, text="Enter The Text :")
text1.place(x=40, y=40)

text2 = Entry(Box, width=30)
text2.place(x=140, y=40)

Button1 = Button(Box, text="Convert", command=speech_to_text)
Button1.place(x=140, y=80)
Button2 = Button(Box, text="Open", command=Open)
Button2.place(x=240, y=80)

Box.mainloop()
