import converter
import tkinter as tk

min_width = 400
min_height = 200


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
        self.input_format = tk.StringVar(master)
        self.input_format.set(self.SYSTEMS[2])
        self.output_format = tk.StringVar(master)
        self.output_format.set(self.SYSTEMS[2])
        self.title_label = tk.Label(text="Number converter", font=('bold', 20))
        self.input_menu_label = tk.Label(text="Input format: ")
        self.input_menu = tk.OptionMenu(
            master, self.input_format, *self.SYSTEMS)
        self.input_label = tk.Label(text="Input:")
        self.input = tk.Entry()
        self.output_menu_label = tk.Label(text="Output format: ")
        self.output_menu = tk.OptionMenu(
            master, self.output_format, *self.SYSTEMS)
        self.output_label = tk.Label(text="=>")
        self.output = tk.Label()
        self.convert_button = tk.Button(
            text="convert", command=self.conversion_handler)
        self.handle_layout()

    # handle layout
    def handle_layout(self):
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(4, minsize=100, weight=1)
        self.title_label.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.input_menu_label.grid(row=1, column=0)
        self.input_menu.grid(row=1, column=1)
        self.output_menu_label.grid(row=1, column=2)
        self.output_menu.grid(row=1, column=3)
        self.input_label.grid(row=2, column=0)
        self.input.grid(row=2, column=1)
        self.output_label.grid(row=2, column=2)
        self.output.grid(row=2, column=3)
        self.convert_button.grid(row=3, column=0, columnspan=4)

    # event handlers for buttons etc.
    def conversion_handler(self):
        value = self.input.get()
        input_type = self.get_format(self.input_format)
        output_type = self.get_format(self.output_format)
        if input_type != "dec":
            value = converter.to_decimal(value, input_type)
        if output_type != "dec":
            value = converter.from_decimal(value, output_type)
        self.output["text"] = value

    # helper functions
    def get_format(self, format):
        f = format.get()
        if f == "bin":
            return 2
        if f == "oct":
            return 8
        if f == "dec":
            return 10
        if f == "hex":
            return 16


if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(min_width, min_height)
    GUI(root)
    root.mainloop()
