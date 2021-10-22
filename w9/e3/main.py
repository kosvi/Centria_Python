import coder
import tkinter as tk


class Morse:

    text_height = 5

    # initialize object for GUI
    def __init__(self, master):
        self.master = master
        self.input_label = tk.Label(text="Input:")
        self.input = tk.Text()
        self.output_label = tk.Label(text="Output:")
        self.output = tk.Text()
        # button frame
        self.button_frame = tk.Frame(master)
        self.to_morse_button = tk.Button(
            self.button_frame, text="Convert to morse", command=self.convert_to_morse)
        self.to_text_button = tk.Button(
            self.button_frame, text="Convert to text", command=self.convert_to_text)
        self.handle_layout()

    # handle layout
    def handle_layout(self):
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.input_label.grid(row=0, column=0)
        self.input.configure(height=self.text_height)
        self.input.grid(row=1, column=0)
        self.button_frame.grid(row=2, column=0)
        self.to_morse_button.grid(row=0, column=0)
        self.to_text_button.grid(row=0, column=1)
        self.output_label.grid(row=3, column=0)
        self.output.configure(height=self.text_height)
        self.output.grid(row=4, column=0)

    # event handlers for buttons etc.
    def convert_to_morse(self):
        text = self.read_input()
        morse = coder.text_to_morse(text)
        self.write_to_output(morse)

    def convert_to_text(self):
        morse = self.read_input()
        text = coder.morse_to_text(morse)
        self.write_to_output(text)

    # helper functions
    def read_input(self):
        return self.input.get(1.0, "end")

    def write_to_output(self, content):
        self.output.delete(1.0, "end")
        self.output.insert(1.0, content)


if __name__ == '__main__':
    root = tk.Tk()
    Morse(root)
    root.mainloop()
