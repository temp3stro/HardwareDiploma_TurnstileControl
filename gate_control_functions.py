#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Device, AngularServo, LED
from gpiozero.pins.pigpio import PiGPIOFactory

# ========== Для чистого PWM без jitter ==========
Device.pin_factory = PiGPIOFactory()

# === Пины ===
SERVO_PIN     = 18  # BCM18, phys 12
RED_LED_PIN   = 23  # BCM23, phys 16
GREEN_LED_PIN = 24  # BCM24, phys 18
BUZZER_PIN    = 22  # BCM22, phys 15

# === Настройка RPi.GPIO для зуммера ===
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.output(BUZZER_PIN, GPIO.HIGH)  # по умолчанию — молчим

def beep(times=1, on_time=0.1, off_time=0.1):
    """Трёхтональный зуммер через RPi.GPIO"""
    for _ in range(times):
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        sleep(on_time)
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        sleep(off_time)

# === Инициализация gpiozero ===
servo     = AngularServo(
    SERVO_PIN,
    min_angle=0, max_angle=180,
    min_pulse_width=0.0005, max_pulse_width=0.0025
)
red_led   = LED(RED_LED_PIN)
green_led = LED(GREEN_LED_PIN)

# === Стартовое положение ===
servo.angle = 0
red_led.on()
green_led.off()
sleep(1)

try:
    # Открытие — сразу на 180°
    red_led.off()
    green_led.off()
    print("Opening…")
    servo.angle = 180
    sleep(0.5)        # даём сервоприводу время дойти до упора
    green_led.on()
    beep(2)
    print("→ OPENED")
    sleep(1)

    # Закрытие — сразу на 0°
    red_led.off()
    green_led.off()
    print("Closing…")
    servo.angle = 0
    sleep(0.5)        # возвращаем в начальное положение
    red_led.on()
    beep(1)
    print("→ CLOSED")

finally:
    servo.detach()
    GPIO.cleanup()
