"""Work from 9am to 5pm
1. Water - play water.mp3, 3.5lt, Drank, log-water.txt
2. Eyes - eye.mp3 - every 35 mins, EyDone, log-eyes.txt
3. Physical Activity - phy.mp3 45 min, ExDone, log-physical.txt"""
import time
from pygame import mixer
import datetime as dt
print("Welcome to Health Management Service")
epoch = time.time()

current_time = time.ctime(epoch)
print("Current time from epoch is-",current_time)

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
print("Current Date and Time",time_string)
year = int(time.strftime("%Y",named_tuple))
month = int(time.strftime("%d",named_tuple))
day = int(time.strftime("%m",named_tuple))
hours = time.strftime("%H", named_tuple)
minute = time.strftime("%M",named_tuple)
sec = time.strftime("%S", named_tuple)




print("Hours is - ",hours)
print("Seconds is-",sec)
if hours == 9 and hours < 17:
    if hours ==9:
        epoch_hours_at_9 = time.time()

    total_seconds = epoch - epoch_hours_at_9
    print("Total seconds spend from 9 AM is -",total_seconds)
    if total_seconds % 1800 == 0:
        mixer.init()
        mixer.music.load("BarsoReMegha.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)
        print("Press Drank after you drink water")
        while True:
            press = input()
            if press == "Drank":
               f = open("water.txt","a")
               #f.write("Water Drank at-",end=" ")
               f.write(time.asctime(time.localtime(time.time())))
               break
    elif total_seconds % 2100 ==0:
        mixer.init()
        mixer.music.load("Virah.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)
        print("Press EyDone after you done Eyes Excercise")
        while True:
            press = input()
            if press == "EyDone":
                f = open("eyes.txt", "a")
                f.write("Eyes Excercise done at-", time.asctime(time.localtime(time.time())))
                break
    elif total_seconds % 2700 ==0:
        mixer.init()
        mixer.music.load("brothers-anthem-tune.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)
        print("Press ExDone after you done Physical Excercise")
        while True:
            press = input()
            if press == "EyDone":
                f = open("physical.txt", "a")
                f.write("Physical excercise done at-", time.asctime(time.localtime(time.time())))
                break








