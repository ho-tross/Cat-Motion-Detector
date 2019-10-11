import RPi.GPIO as GPIO
import time
from subprocess import call
import vlc
import  random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
while True:
    i = GPIO.input(11)
    if i ==0:
        print("Screen off", i)
        call(["/usr/bin/vcgencmd", "display_power", "0"])
        time.sleep(1)
    elif i ==1:
        print("Screen on", i)
        call(["/usr/bin/vcgencmd", "display_power", "1"])
        radnumb = random.randint(0,29)
        vidtitle = "/home/python/catvideo-" + radnumb + "-of-56.mkv"
        media = vlc.MediaPlayer(vidtitle)
        media.play()
        time.sleep(120)
        media.stop()
