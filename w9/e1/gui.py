from tkinter import *
import task

class GUI:
  def __init__(self, task_factory):
    self.window = Tk()
    self.calculation = task_factory
    self.set_calculation()
    self.feedback = ""
    self.correct = 0
    self.wrong = 0
    self.window.rowconfigure([0, 1], minsize=100, weight=1)
    self.window.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)
    self.draw_content()
    self.window.mainloop()

  def set_calculation(self):
    self.calculation.new_task()

  def check_solution(self):
    try:
      ans = self.ans.get()
      if ans==self.calculation.ans:
        self.feedback = "CORRECT!"
        self.correct += 1
      else:
        self.feedback = "WRONG!"
        self.wrong += 1
    except:
      print("incorrect input")
    print(f"{self.correct} correct answers and {self.wrong} wrong answers")
    self.set_calculation()
    self.draw_content()

  def clear_content(self):
    for content in self.window.winfo_children():
      content.destroy()

  def draw_content(self):
    self.clear_content()
    self.val1 = Label(master=self.window, text=self.calculation.value1)
    self.val1.grid(row=0, column=0)
    self.calc = Label(master=self.window, text=self.calculation.calc)
    self.calc.grid(row=0, column=1)
    self.val2 = Label(master=self.window, text=self.calculation.value2)
    self.val2.grid(row=0, column=2)
    self.equalsign = Label(master=self.window, text="=")
    self.equalsign.grid(row=0, column=3)
    self.ans = IntVar()
    self.ansEntry = Entry(master=self.window, textvariable=self.ans)
    self.ansEntry.grid(row=0, column=4)
    self.button = Button(master=self.window, text="check", command=self.check_solution)
    self.button.grid(sticky="NE", row=1, column=4)
    self.feedback_label = Label(master=self.window, text=self.feedback)
    self.feedback_label.grid(row=1, column=0, columnspan=4)
    self.feedback_label.after(2000, lambda: self.feedback_label.config(text=""))

