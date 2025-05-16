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

def close_gate(step=5, delay=0.2):
    """Move servo toward 0° until CLOSED limit switch triggers"""
    print("Closing…")
    servo.angle = 90
    sleep(0.5)
    while not sw_closed.is_pressed and servo.angle and servo.angle > 0:
        servo.angle -= step
        print(f"  angle={servo.angle:.0f}°", end="\r")
        sleep(delay)
    print("\n→ Gate CLOSED" if sw_closed.is_pressed else "\n‼️ Failed to close")

def open_gate(step=5, delay=0.2):
    """Move servo toward 180° until OPEN limit switch triggers"""
    print("Opening…")
    servo.angle = 90
    sleep(0.5)
    while not sw_open.is_pressed and servo.angle and servo.angle < 180:
        servo.angle += step
        print(f"  angle={servo.angle:.0f}°", end="\r")
        sleep(delay)
    print("\n→ Gate OPENED" if sw_open.is_pressed else "\n‼️ Failed to open")

if __name__ == "__main__":
    try:
        close_gate()
        sleep(1)
        open_gate()
    finally:
        servo.detach()
