# use Tkinter to show a digital clock
# tested with Python24    vegaseat    10sep2006
from Tkinter import *
import time
from time import strftime

canTime = 0
time1 = time.time()
timerSec = 0
homeScore = 0
awayScore = 0
def set_text(text):
    clock.delete(0,END)
    clock.insert(0,text)
    return
def format(t):
    sec = t
    mins = sec // 60
    seconds = sec % 60
    if seconds >= 10:
        if mins == 0:
            return str(mins) + '0:' + str(seconds)
        else:
            return str(mins) + ':' + str(seconds)
    else:
        if mins == 0:
            return str(mins) + '0:0' + str(seconds)
        else:
            return str(mins) + ':0' + str(seconds)
def startStopTimer():
    global canTime
    if canTime == 0:
        canTime = 1
    else:
        canTime = 0
def setClock():
    global timerSec
    global time1

    input = clock.get()
    input = input.split(':')
    timerSec = 0 + 60 * int(input[0]) + int(input[1])
    time1 = time.time()

timeFile = open('game_time.txt','w')
homeScoreFile = open('home_score.txt','w')
awayScoreFile = open('away_score.txt','w')
root = Tk()
clock = Entry(root)
clock.pack()
set_text("00:00")
def tick():
    global time1
    global timerSec
    global canTime
    global timeFile
    # get the current local time from the PC
    time2 = time.time()
    # if time string has changed, update it
    if canTime == 1 and time2 > time1 + 1:
        timerSec = timerSec + 1
        timeString = format(timerSec)
        set_text(timeString)
        time1 = time2
        timeFile.seek(0)
        timeFile.write(timeString)
        timeFile.truncate()
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(10, tick)
tick()

def homePlus():
    global homeScore
    homeScore = homeScore + 10
    homeScoreFile.seek(0)
    homeScoreFile.write(str(homeScore))
    homeScoreFile.truncate()
    set_homescore_text(str(homeScore))
def awayPlus():
    global awayScore
    awayScore = awayScore + 10
    awayScoreFile.seek(0)
    awayScoreFile.write(str(awayScore))
    awayScoreFile.truncate()
    set_awayscore_text(str(awayScore))
def homeMinus():
    global homeScore
    homeScore = homeScore - 10
    homeScoreFile.seek(0)
    homeScoreFile.write(str(homeScore))
    homeScoreFile.truncate()
    set_homescore_text(str(homeScore))
def awayMinus():
    global awayScore
    awayScore = awayScore - 10
    awayScoreFile.seek(0)
    awayScoreFile.write(str(awayScore))
    awayScoreFile.truncate()
    set_awayscore_text(str(awayScore))

def set_homescore_text(text):
    homeScoreEntry.delete(0,END)
    homeScoreEntry.insert(0,text)
    return
def set_awayscore_text(text):
    awayScoreEntry.delete(0,END)
    awayScoreEntry.insert(0,text)
    return
def set_score():
    global homeScore
    global awayScore
    homeScore = int(homeScoreEntry.get())
    awayScore = int(awayScoreEntry.get())
    awayScoreFile.seek(0)
    awayScoreFile.write(str(awayScore))
    awayScoreFile.truncate()
    homeScoreFile.seek(0)
    homeScoreFile.write(str(homeScore))
    homeScoreFile.truncate()
Button(root, text='Start/Stop Timer', command=startStopTimer).pack()
Button(root, text='Set Timer', command=setClock).pack()
Label(root, text="Home Score").pack()
homeScoreEntry = Entry(root)
homeScoreEntry.pack()
Label(root, text="Away Score").pack()
awayScoreEntry = Entry(root)
awayScoreEntry.pack()
set_awayscore_text("0")
set_homescore_text("0")
Button(root, text='Home +10', command=homePlus).pack()
Button(root, text='Home -10', command=homeMinus).pack()
Button(root, text='Away +10', command=awayPlus).pack()
Button(root, text='Away -10', command=awayMinus).pack()
Button(root, text='Set Score', command=set_score).pack()
root.mainloop()
