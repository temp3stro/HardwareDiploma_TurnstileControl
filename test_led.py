#!/usr/bin/env python3
from gpiozero import LED
from time import sleep

# LED pins
red = LED(23)
green = LED(24)

# Blink test
red.on()
sleep(1)
red.off()
green.on()
sleep(1)
green.off()
