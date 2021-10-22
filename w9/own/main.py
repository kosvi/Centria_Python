import converter
import tkinter as tk

min_width = 40
min_height = 20


class GUI:

    # https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter
    SYSTEMS = [
      "bin",
      "oct",
      "dec",
      "hex"
    ]

    # initialize object for GUI
    def __init__(self, master):
        self.master = master
        self.options = tk.StringVar(master)
        self.options.set(self.SYSTEMS[2])
        self.title_label = tk.Label(text="Number converter", font=('bold', 20))
        self.input_menu = tk.OptionMenu(master, self.options, *self.SYSTEMS)
        self.input_label = tk.Label(text="Input:")
        self.input = tk.Entry()
        self.output_label = tk.Label(text="=>")
        self.output = tk.Label()
        self.convert_button = tk.Button(
            text="convert", command=self.test_handler)
        self.handle_layout()

    # handle layout
    def handle_layout(self):
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(4, minsize=100, weight=1)
        self.title_label.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.input_menu.grid(row=1, column=0)
        self.input_label.grid(row=2, column=0)
        self.input.grid(row=2, column=1)
        self.output_label.grid(row=2, column=2)
        self.output.grid(row=2, column=3)
        self.convert_button.grid(row=3, column=0, columnspan=1)

    # event handlers for buttons etc.
    def test_handler(self):
        value = self.input.get()
        foo = converter.from_decimal(value, 2)
        self.output["text"] = foo

    # helper functions


if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(min_width, min_height)
    GUI(root)
    root.mainloop()
