#!/usr/bin/python3
import RPi.GPIO as GPIO
import board
import busio
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
FAN_PIN = 17
GPIO.setup(FAN_PIN, GPIO.OUT)
FAN_PIN_STATE = GPIO.input(FAN_PIN)
if FAN_PIN_STATE == 0:
    print("ON")
else:
    print("OFF")
