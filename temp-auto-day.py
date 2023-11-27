#!/usr/bin/python3
import RPi.GPIO as GPIO
import pymongo
import sys
from pymongo import MongoClient
import board
import busio
import adafruit_sht31d
import datetime
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)
h = float("{0:.2f}".format(sensor.relative_humidity))
t = float("{0:.2f}".format(sensor.temperature))
url = 'mongodb+srv://tsvetanovemil87:W6nnG4AX2hJBCVNR@cluster0.jfxqd29.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(url)
db = client.room
collection = db.env
query_data = {
    'time': datetime.datetime.now(),
    'temperature': t+2,
    'humidity': h
}
result = collection.insert_one(query_data)
minTemp = int(sys.argv[1])
maxTemp = int(sys.argv[2])
modifiedTemp = t+2
if modifiedTemp > maxTemp:
    GPIO.output(17, True)
elif modifiedTemp < minTemp:
    GPIO.output(17, False)
