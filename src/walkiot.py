import pygame
pygame.mixer.init()

for i in range(pygame.mixer.get_num_channels()):
    c = pygame.mixer.Channel(i)
    c.set_volume(1)

def sync_play_sound(fn):
    pygame.mixer.music.load(fn)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

from gpiozero import Button
from time import sleep

def connect_to_button(pin, cb):
    def f():
        print("Pressed pin " + str(pin))
        cb(pin)

    btn = Button(pin)
    btn.when_pressed = f
    print("Connected to pin " + str(pin))
    return btn


class KeySound(object):
    def __init__(self):
        self.keys = {
           # Piano
            5: "sounds/piano/do.wav",
            6: "sounds/piano/re.wav",
           13: "sounds/piano/mi.wav",
           26: "sounds/piano/fa.wav",
            0: "sounds/piano/sol.wav",

           # Cow
           11: "i.wav",
           # Phone
           9: "i.wav",
           # Switch book/music?
           10: "i.wav",
           # Rolling thingy
           22: "i.wav",
           # Sun button
           27: "i.wav",
           # Square button
           16: "i.wav",
           # Triangle button
           1: "i.wav",
        }

        self._btns = [connect_to_button(pin, self.on_key_press)
                        for pin in self.keys.keys()]

    def on_key_press(self, pin):
        print("Play " + self.keys[pin])
        sync_play_sound(self.keys[pin])

foo = KeySound()
while True:
    sleep(1)


#leds = [17,          # Sun button
#        20,
#        7,
#        ]
#
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
## #GPIO.setwarnings(False)
#for pin in leds:
#    GPIO.setup(pin,GPIO.OUT)
#    GPIO.output(pin,GPIO.HIGH)
#

