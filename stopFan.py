#!/usr/bin/python3
import RPi.GPIO as GPIO
import board
import busio
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, True)
