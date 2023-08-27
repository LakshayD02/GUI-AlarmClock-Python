from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image      #Installation - pip install Pillow

from datetime import datetime
from time import sleep

from threading import Thread, Lock
_db_lock = Lock()

from pygame import mixer

#Writing code for Windows
window = Tk()
window.title("Alarm Clock with GUI")
window.geometry('390x218')
window.configure(bg="white")

#Frames
frame1= Frame(window,width=500,height=10, bg="white")      #Code for Frame Line
frame1.grid(row=0, column=0)

frame2= Frame(window,width=500,height=200, bg="black")      #Code for Frame Body
frame2.grid(row=1, column=0)

#Configuring Frame Body
img = Image.open('Clock.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame2, height=150, image=img, bg="black")
app_image.place(x=10, y=10)

name = Label(frame2, text="Alarm Clock", height=1, font="Ivy 20 bold", bg="black", fg="white")
name.place(x=130,y=15)

#Creating Hour Part of Clock
hour = Label(frame2, text="Hour", height=1, font="Ivy 10 bold", bg="black", fg="cyan")
hour.place(x=128,y=60)

#Creating Dropbox for Hour (Combobox)
clock_hour = Combobox(frame2, width=2, font='arial 15', height=10)
clock_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
clock_hour.current(0)
clock_hour.place(x=130, y=90)

#Creating Minute Part of Clock
min = Label(frame2, text="Min", height=1, font="Ivy 10 bold", bg="black", fg="cyan")
min.place(x=180,y=60)

#Creating Dropbox for Minutes (Combobox)
clock_min = Combobox(frame2, width=2, font='arial 15')
clock_min['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27",
                        "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
clock_min.current(0)
clock_min.place(x=180, y=90)

#Creating Seconds Part of Clock
sec = Label(frame2, text="Sec", height=1, font="Ivy 10 bold", bg="black", fg="cyan")
sec.place(x=230,y=60)

#Creating Dropbox for Seconds (Combobox)
clock_sec = Combobox(frame2, width=2, font='arial 15')
clock_sec['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27",
                        "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
clock_sec.current(0)
clock_sec.place(x=230, y=90)

#Creating Period Part of Clock
period = Label(frame2, text="Period", height=1, font="Ivy 10 bold", bg="black", fg="cyan")
period.place(x=280,y=60)

#Creating Dropbox for Period (Combobox)
clock_period = Combobox(frame2, width=3, font='arial 15')
clock_period['values'] = ("AM", "PM")
clock_period.current(0)
clock_period.place(x=280, y=90)

def activate_alarm():
    t = Thread(target=alarm)
    t.start()
    
def deactivate_alarm():
    print('Deactivate Alarm : ', selected.get())
    mixer.music.stop()

selected = IntVar()

rad1 = Radiobutton(frame2, font="arial 11 bold", value=1, text="Activate", bg="black", fg="white", command=activate_alarm, variable=selected)
rad1.place(x=130, y=140)

def sound_alarm():
    mixer.music.load('Alarm.mp3')
    mixer.music.play()
    selected.set(0)
    
    rad2 = Radiobutton(frame2, font="arial 11 bold", value=2, text="Deactivate", bg="black", fg="white", command=deactivate_alarm, variable=selected)
    rad2.place(x=190, y=140)

    
def alarm():
    while True:
        control = selected.get()
        print(control)
        
        alarm_hour= clock_hour.get()
        alarm_minute = clock_min.get()
        alarm_sec = clock_sec.get()
        alarm_period = clock_period.get()
        alarm_period = str(alarm_period).upper()
        
        now = datetime.now()
        
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")
        
        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("Time to take a break!")
                            sound_alarm()
        
        sleep(1)
        
mixer.init()

window.mainloop()