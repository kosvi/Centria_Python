from clock import Clock

class AlarmClock(Clock):

  def __init__(self):
    Clock.__init__(self)
    self.alarm_off = True

  def set_alarm(self, alarm):
    self.alarm = alarm
    self.alarm_off = False

  def tick(self):
    super().tick()
    if self.alarm_off:
      return False
    if self.alarm == super().get_time():
      self.alarm_off = True
      return True
    return False
