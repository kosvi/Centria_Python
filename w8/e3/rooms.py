from room import Room

class Kitchen(Room):

  def __init__(self, size=0, renovated=2000):
    super().__init__(size)
    self.renovated = renovated

  def get_info(self):
    s = super().get_info("Kitchen") + f" and was renovated {self.renovated}"
    return s

class LivingRoom(Room):

  def __init__(self, size=0, window_direction=""):
    super().__init__(size)
    self.window_direction = window_direction

  def get_info(self):
    s = super().get_info("Living room") + f" and window is facing {self.window_direction}"
    return s

class Bedroom(Room):

  def __init__(self, size=0, beds=1):
    super().__init__(size)
    self.beds = beds

  def get_info(self):
    s = super().get_info("Bedroom") + f" and has {self.beds} beds"
    return s
