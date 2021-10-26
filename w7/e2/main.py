#!/usr/bin/python3

from alarmclock import AlarmClock
from time import sleep

ac = AlarmClock()
ac.set_alarm(5)
while ac.get_time()<10:
  if ac.tick():
    print("ALARM!!!")
  print(f"time: {ac.get_time()}")
  sleep(1)
