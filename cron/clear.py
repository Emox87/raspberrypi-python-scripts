#!/usr/bin/python
from crontab import CronTab
cron = CronTab(user='pi')
cron.remove_all()
cron.write()
