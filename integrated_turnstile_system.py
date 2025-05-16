#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Device, AngularServo, Button, LED
from gpiozero.pins.pigpio import PiGPIOFactory

# Use pigpio for cleaner PWM
Device.pin_factory = PiGPIOFactory()

# Pin setup
SERVO_PIN     = 18
SW_CLOSED_PIN = 17
SW_OPEN_PIN   = 27
RED_LED_PIN   = 23
GREEN_LED_PIN = 24
BUZZER_PIN    = 22

# Setup RPi.GPIO for buzzer
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.output(BUZZER_PIN, GPIO.HIGH)

def beep(times=1, on_time=0.1, off_time=0.1):
    for _ in range(times):
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        sleep(on_time)
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        sleep(off_time)

# Initialize devices
servo = AngularServo(SERVO_PIN, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025)
sw_closed = Button(SW_CLOSED_PIN, pull_up=True)
sw_open = Button(SW_OPEN_PIN, pull_up=True)
red_led = LED(RED_LED_PIN)
green_led = LED(GREEN_LED_PIN)

angle = 0
servo.angle = angle
sleep(1)

def open_turnstile(step=5, delay=0.2):
    global angle
    red_led.off(); green_led.off()
    print("Opening turnstile…")
    while not sw_open.is_pressed and angle < 180:
        angle = min(angle + step, 180)
        servo.angle = angle
        print(f"  Opening → angle = {angle}°", end="\r")
        sleep(delay)
    if sw_open.is_pressed:
        green_led.on()
        beep(2)
        print("\n→ OPENED")
    else:
        beep(1)
        print("\n‼️ Failed to open")

def close_turnstile(step=5, delay=0.2):
    global angle
    red_led.off(); green_led.off()
    print("Closing turnstile…")
    while not sw_closed.is_pressed and angle > 0:
        angle = max(angle - step, 0)
        servo.angle = angle
        print(f"  Closing → angle = {angle}°", end="\r")
        sleep(delay)
    if sw_closed.is_pressed:
        red_led.on()
        beep(1)
        print("\n→ CLOSED")
    else:
        beep(1)
        print("\n‼️ Failed to close")

if __name__ == "__main__":
    try:
        open_turnstile()
        sleep(1)
        close_turnstile()
    finally:
        servo.detach()
        GPIO.cleanup()
