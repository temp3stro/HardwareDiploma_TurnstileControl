#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.output(BUZZER_PIN, GPIO.HIGH)

def beep(times=3, length=0.1):
    for _ in range(times):
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(length)
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(length)

if __name__ == "__main__":
    try:
        print("Beeping 3 times…")
        beep(3, 0.2)
        print("One long tone…")
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
    finally:
        GPIO.cleanup()
