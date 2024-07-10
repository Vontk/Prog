import tkinter as tk

calculation = ''


def input_argument(symbol):
    pass


def evaluate_argument():
    pass


def clear_argument():
    pass


# tk.Tk() constructs a main app window on default settings, it's an objet made using a class, we store it on 'root'
root = tk.Tk()
root.title('Calculator')
root.geometry('500x500')
# tk.Text() creates a text widget class, used to input and display text on the gui
text_result = tk.Text(root, height=2, width=16, font=('Arial', 24))
# this doesn't create the text box, because we didn't specify position, but text_result.pack() will create it,
# try argument fill, expand or side <text_result.pack(fill=tk.BOTH, expand=True)>
# method that runs the window until it's closed
root.mainloop()
