import time
import pygame
from pygame import mixer

# Music did not played hence I have printed it as well.
def playMusic(file):
    print(file)
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.9)
    mixer.music.play()


def IsOfficeTime(currenttime):
    if currenttime > '09:00:00' and currenttime < '17:00:01':
        return True
    else:
        return False


NumberofWaterRemaining = 18

WaterAfterEvery = 1200  # Seconds  - 20 minutes
EyeExerciseAfterEvery = 1800  # Seconds - 30 minutes
PhysicalExerciseAfterEvery = 2700  # Seconds  - 45 minutes

waterMp3 = 'BarsoReMegha.mp3'
eyesMp3 = 'Virah.mp3'
PhysicalMp3 = 'brothers-anthem-tune.mp3'

currenttime = time.strftime('%H:%M:%S')
WaterTakenAt = time.time()
EyeExerciseAt = time.time()
PhysicalExerciseAt = time.time()

SleepTime = 60  # Sleep time in seconds It will check after every 60 seconds.

while (IsOfficeTime(currenttime)):
    #     Check for water
    if NumberofWaterRemaining > 0:
        if (time.time() - WaterTakenAt) > WaterAfterEvery:  # water after every 20 minutes
            print("Time to drink water")
            while True:
                playMusic(waterMp3)
                if input("Enter Done if you had water: ").lower() == "done":
                    WaterTakenAt = time.time()
                    NumberofWaterRemaining -= 1
                    break
        if time.time() - EyeExerciseAt > EyeExerciseAfterEvery:
            print("Time to do eye exercise")
            while True:
                playMusic(eyesMp3)
                if input("Enter Done if you done eye exercise : ").lower() == "done":
                    EyeExerciseAt = time.time()
                    break
        if time.time() - PhysicalExerciseAt > PhysicalExerciseAfterEvery:
            print("Time to do Physical exercise")
            while True:
                playMusic(PhysicalMp3)
                if input("Enter Done if you done Physical exercise : ").lower() == "done":
                    PhysicalExerciseAt = time.time()
                    break

    time.sleep(SleepTime)
    currenttime = time.strftime('%H:%M:%S')