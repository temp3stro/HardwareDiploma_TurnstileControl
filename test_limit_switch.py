#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Test limit switch on GPIO17 (BCM17)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Limit switch test: press/release the lever…")
try:
    while True:
        if GPIO.input(17) == GPIO.LOW:
            print("→ Switch CLOSED (pressed)")
        else:
            print("→ Switch OPEN (released)")
        time.sleep(0.5)
finally:
    GPIO.cleanup()
