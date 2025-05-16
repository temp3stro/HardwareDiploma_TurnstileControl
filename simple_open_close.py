#!/usr/bin/env python3
from gpiozero import AngularServo, Button
from time import sleep

# Pin configuration
SERVO_PIN = 18
SW_CLOSED = 17
SW_OPEN = 27

servo = AngularServo(SERVO_PIN, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025)
sw_closed = Button(SW_CLOSED, pull_up=True)
sw_open = Button(SW_OPEN, pull_up=True)

# Initial closed position
servo.angle = 0
sleep(1)

print("Opening turnstile…")
while not sw_open.is_pressed:
    servo.angle = min(servo.angle + 5, 180)
    sleep(0.2)
print("→ OPENED!")
sleep(1)

print("Closing turnstile…")
while not sw_closed.is_pressed:
    servo.angle = max(servo.angle - 5, 0)
    sleep(0.2)
print("→ CLOSED!")
servo.detach()
