from clock import Clock

class AlarmClock(Clock):

  def set_alarm(self, alarm):
    self.alarm = alarm

  def tick(self):
    super().tick()
    if self.alarm == super().get_time():
      return True
    return False
