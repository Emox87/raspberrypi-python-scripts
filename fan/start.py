#!/usr/bin/python3
import RPi.GPIO as GPIO
import board
import busio
from pymongo import MongoClient
import datetime
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, False)
url = 'mongodb+srv://tsvetanovemil87:W6nnG4AX2hJBCVNR@cluster0.jfxqd29.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(url)
db = client.room
collection = db.fan
query_data = {
        'time': datetime.daytime.now(),
        'log': 'Fan has been started'
}
result = collection.insert_one(query_data)
client.close()
print("ON")
