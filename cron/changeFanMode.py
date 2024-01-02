#!/usr/bin/python3
import sys
from crontab import CronTab
import pymongo
from pymongo import MongoClient
from bson import ObjectId

mode = sys.argv[1]

tempMin = 18
tempMax = 25

baseCommand = 'python /home/pi/scripts/raspberrypi-python-scripts/cron/auto.py'
execCommand = ''

if mode == 'cold':
    execCommand = f'{baseCommand} 18 20'
elif mode == 'normal':
    execCommand = f'{baseCommand} 20 22'
elif mode == 'hot':
    execCommand = f'{baseCommand} 23 25'
elif mode == 'clear':
    execCommand = 'python /home/pi/scripts/raspberrypi-python-scripts/sensor/mongoSendData.py'

cron = CronTab(user='pi')
job = cron.remove_all()
job = cron.new(command=execCommand)
job.minute.every(30)
cron.write()

url = "mongodb+srv://tsvetanovemil87:W6nnG4AX2hJBCVNR@cluster0.jfxqd29.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

db = client.room
collection = db.settings
collection.find_one_and_update({"_id": ObjectId("657b0debb97b3f3e45f2ce93")}, {'$set': { "mode": mode }})
print(f"Mode has been updated to {mode}")
