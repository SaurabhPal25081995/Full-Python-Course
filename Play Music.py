from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("Virah.mp3")

# Setting the volume
mixer.music.set_volume(0.1)

# Start playing the song
#mixer.music.set_pos(45)
mixer.music.play(-1)  # play(-1) for infinite loop

print("To Pause press p -   \nTo Resume press r -  \nTo Exit press e  ")

while True:
    query = input()

    # Pausing the music
    if query =='p':
        print("Paused.")
        mixer.music.pause()

    #Resuming the music
    elif query =='r':
        print("Resuming...")
        mixer.music.unpause()

    #Stop the music
    elif query =='e':
        print("Exit")
        mixer.music.stop()
        break
