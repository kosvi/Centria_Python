#!/usr/bin/python3

from alarmclock import AlarmClock
from time import sleep

ac = AlarmClock()
print("No alarm set:")
while ac.get_time()<5:
  if ac.tick():
    print("ALARM!!!")
  print(f"time: {ac.get_time()}")
  sleep(1)
ac.reset()
ac.set_alarm(5)
print("Alarm set to 5:")
while ac.get_time()<10:
  if ac.tick():
    print("ALARM!!!")
  print(f"time: {ac.get_time()}")
  sleep(1)
