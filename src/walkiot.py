import pygame
pygame.mixer.init()

# for i in range(pygame.mixer.get_num_channels()):
#     c = pygame.mixer.Channel(i)
#     c.set_volume(1)

def sync_play_sound(fn):
    print("Play " + fn)
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
    def _book_keys(self):
        return {
           # Piano
            5: "sounds/nums/1.wav",
            6: "sounds/nums/2.wav",
           13: "sounds/nums/3.wav",
           26: "sounds/nums/4.wav",
            0: "sounds/nums/5.wav",

           # Cow
           11: "sounds/cow.wav",
           # Phone
           9: ["sounds/phone.wav", "sounds/hola.wav"],
           # Rolling thingy
           22: "sounds/weee.wav",
           # Sun button
           27: "sounds/hola.wav",
           # Triangle button
           1: "sounds/tada.wav",
        }

    def _music_keys(self):
        return {
           # Piano
            5: "sounds/piano/do.wav",
            6: "sounds/piano/re.wav",
           13: "sounds/piano/mi.wav",
           26: "sounds/piano/fa.wav",
            0: "sounds/piano/sol.wav",

           # Cow
           11: "sounds/cow.wav",
           # Phone
           9: ["sounds/phone.wav", "sounds/hola.wav"],
           # Rolling thingy
           22: "sounds/weee.wav",
           # Sun button
           27: "sounds/hola.wav",
           # Triangle button
           1: "sounds/tada.wav",
        }

    def __init__(self):
        self._book_music_switch = Button(10)
        # Pins are the same for both modes, arbitrarily pick one
        pins = self._music_keys()
        self._btns = [connect_to_button(pin, self.on_key_press)
                        for pin in pins.keys()]

    def book_mode_enabled(self):
        return self._book_music_switch.is_active

    def _active_pin_map(self):
        if self.book_mode_enabled():
            return self._book_keys()
        else:
            return self._music_keys()

    def on_key_press(self, pin):
        pinmap = self._active_pin_map()
        if isinstance(pinmap, (list,)):
            for snd in pinmap:
                sync_play_sound(snd)
        else:
            sync_play_sound(pinmap)

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

