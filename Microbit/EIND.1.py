import time
import music

from microbit import *
seconds = 0
while True:
    
    if button_a.is_pressed():
        seconds += 10
        display.show(seconds)
        sleep(1000)
        display.clear()


    elif button_b.is_pressed():
        seconds += 1
        display.show(seconds)
        sleep(1000)
        display.clear()


    if accelerometer.was_gesture('shake'):
        while seconds > -1:
            display.show(seconds)
            sleep(1000)
            seconds -= 1
            if seconds == 0:
                music.play(["B6", "B6", "B6", "B6", "B6", "B6", "B6", "B6"])
    
