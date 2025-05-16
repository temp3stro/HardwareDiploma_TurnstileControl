#!/usr/bin/env python3
from gpiozero import AngularServo, Button
from time import sleep

# Servo on BCM18
servo = AngularServo(18, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)
sw_closed = Button(17, pull_up=True)

print("Servo sweep test: moving from 135° to 0° until switch triggers…")
servo.angle = 135
sleep(1)

for angle in range(135, -1, -5):
    servo.angle = angle
    print(f"Setting angle {angle}°", end="\r")
    sleep(0.2)
    if sw_closed.is_pressed:
        print(f"\n→ Switch triggered at {angle}°")
        break
else:
    print("\n‼️ Switch did not trigger, check position")
servo.detach()
