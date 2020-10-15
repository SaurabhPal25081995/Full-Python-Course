import vlc
import time

# creating vlc media player object
media_player = pyvlc.MediaPlayer()

# media object
media = vlc.Media("bahu.mp4")

# setting media to media player
media_player.set_media(media)

# start playing video
media_player.play()

time.sleep(5)