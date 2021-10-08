# Add your Python code here. E.g.
from microbit import *


while True:
    if  button_a.is_pressed():
        display.scroll('IK BEN MOSAWER')
    elif button_b.is_pressed():
            egel =Image("04040:46664:08680:46664:06060")
            display.show(egel)
            sleep(2000)
    else:
        display.scroll('HELLO YOU!')
        
        
    display.clear()
    sleep(2000)
