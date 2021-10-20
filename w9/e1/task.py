from random import randint

class Task:

  def __init__(self):
    self.val1 = 0
    self.val2 = 0
    self.calc = '+'
    self.ans = 0

  def new_task(self):
    calculations = ['+', '-', '*', '/']
    calculation = calculations[randint(0,len(calculations)-1)]
    self.calc = calculation
    val1 = randint(-100,100)
    val2 = randint(-100,100)
    if calculation=='+':
      self.ans = val1 + val2
    elif calculation=='-':
      self.ans = val1 - val2
    elif calculation=='*':
      val1 = randint(0,10)
      val2 = randint(0,10)
      self.ans = val1 * val2
    elif calculation=='/':
      val2 = randint(1,10)
      while val1 % val2 != 0:
        # cheap and dirty
        val1 = randint(0, 100)
      self.ans = int(val1 / val2)
    self.value1 = val1
    self.value2 = val2
