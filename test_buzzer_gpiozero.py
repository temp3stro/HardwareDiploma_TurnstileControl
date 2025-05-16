#!/usr/bin/env python3
from gpiozero import Buzzer
from time import sleep

# Buzzer on BCM22
buzzer = Buzzer(22)

# Single beep
buzzer.beep(on_time=0.1, off_time=0.1, n=1)
sleep(0.5)

# Triple beep
buzzer.beep(on_time=0.1, off_time=0.1, n=3)
sleep(1)
buzzer.off()
