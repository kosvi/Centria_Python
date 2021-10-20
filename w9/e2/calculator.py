from tkinter import *

class Calculator:

  # Initialize all components for the calculator
  def __init__(self, master):
    self.master = master
    self.val1 = Entry(master=master)
    self.val2 = Entry(master=master)
    self.plus_btn = Button(master=master, text='+', command=self.sum)
    self.minus_btn = Button(master=master, text='-', command=self.difference)
    self.multiply_btn = Button(master=master, text='*', command=self.multiply)
    self.divide_btn = Button(master=master, text='/', command=self.divide)
    self.ans = Label(master=master, text="")
    self.create_layout()

  # Handle proper layout for the calculator
  def create_layout(self):
    root.rowconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    self.val1.grid(row=0, column=0, columnspan=2)
    self.val2.grid(row=0, column=2, columnspan=2)
    self.plus_btn.grid(row=1, column=0)
    self.minus_btn.grid(row=1, column=1)
    self.multiply_btn.grid(row=1, column=2)
    self.divide_btn.grid(row=1, column=3)
    self.ans.grid(row=2, column=0, columnspan=4)

  # Commands for the buttons
  def sum(self):
    val1, val2 = self.get_values()
    if type(val1) == float:
      self.show_ans(val1+val2)
  def difference(self):
    val1, val2 = self.get_values()
    if type(val1) == float:
      self.show_ans(val1-val2)
  def multiply(self):
    val1, val2 = self.get_values()
    if type(val1) == float:
      self.show_ans(val1*val2)
  def divide(self):
    val1, val2 = self.get_values()
    if type(val1) == float:
      if val2!=0:
        self.show_ans(val1/val2)
      else:
        self.show_ans("ERROR: divide by zero")

  # helper function to output answer
  def show_ans(self, ans):
    self.ans["text"] = str(ans)

  # helper function to get input values
  def get_values(self):
    try:
      val1 = float(self.val1.get())
      val2 = float(self.val2.get())
      return val1, val2
    except:
      print("incorrect input")
      self.show_ans("incorrect input")
      return "error", 1

# Start the calculator if not being imported
if __name__ == '__main__':
  root = Tk()
  Calculator(root)
  root.mainloop()