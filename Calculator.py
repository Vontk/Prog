import tkinter as tk

argument = ''


def input_argument(button_input):
    global argument
    argument += str(button_input)
    # this method deletes the text field of the tkinter text widget, the method takes the input (index, index)
    # and for reference 1.0 represents first position while tk.END represents the end, can be replaced with 'end'
    text_result.delete(1.0, tk.END)
    # then the method insert, replaces the text widget with the new argument
    text_result.insert(tk.END, argument)


def evaluate_argument():
    global argument
    try:
        result = str(eval(argument))
        # if we want the argument to be the calculated number, then <arg = res> if you want it to be cleared <arg = ''>
        argument = result
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)
    # if this results in an error, then the code will run the except
    except SyntaxError:
        clear_argument()
        text_result.insert(1.0, 'Syntax Error')
    except ZeroDivisionError:
        clear_argument()
        text_result.insert(1.0, 'Zero Division Error')
    except ValueError:
        clear_argument()
        text_result.insert(1.0, 'Overflow error; too many characters')
    except OverflowError:
        clear_argument()
        text_result.insert(1.0, 'Overflow error; too many characters')
    except TypeError:
        clear_argument()
        text_result.insert(1.0, 'Syntax Error')
def clear_argument():
    global argument
    argument = ''
    text_result.delete(1.0, tk.END)


# tk.Tk() constructs a main app window on default settings, it's an objet made using a class, we store it on 'root'
root = tk.Tk()
root.title('Calculator')
root.geometry('300x275')
# tk.Text() creates a text widget class, used to input and display text on the gui
# this doesn't create the text box, because we didn't specify position, but text_result.pack() will create it,
# try argument fill, expand or side, like this: <text_result.pack(fill=tk.BOTH, expand=True)>
text_result = tk.Text(root, height=2, width=16, font=('Arial', 24))
# tk geometry method, it's used to place widgets within a grid-based layout system
# the parameter dictates how many columns the widget spans.
text_result.grid(columnspan=5)
# individual buttons, the argument for the method takes (window, text = '', command = function), the command attribute
# expects a function (not the return of a function), lambda turns an otherwise evaluated function into a regular
# function object, waiting to be evaluated (so, actually a function)
# (which can be used on the command attribute and would work as you would expect just calling the function to work)
button_1 = tk.Button(root, text='1', command=lambda: input_argument('1'), width=5, font=('Arial', 14))
# this sets the button to be on the previously created grid
button_1.grid(row=2, column=1)
# now repeat the same for other numbers and operators
button_2 = tk.Button(root, text='2', command=lambda: input_argument('2'), width=5, font=('Arial', 14))
button_2.grid(row=2, column=2)
button_3 = tk.Button(root, text='3', command=lambda: input_argument('3'), width=5, font=('Arial', 14))
button_3.grid(row=2, column=3)
button_4 = tk.Button(root, text='4', command=lambda: input_argument('4'), width=5, font=('Arial', 14))
button_4.grid(row=3, column=1)
button_5 = tk.Button(root, text='5', command=lambda: input_argument('5'), width=5, font=('Arial', 14))
button_5.grid(row=3, column=2)
button_6 = tk.Button(root, text='6', command=lambda: input_argument('6'), width=5, font=('Arial', 14))
button_6.grid(row=3, column=3)
button_7 = tk.Button(root, text='7', command=lambda: input_argument('7'), width=5, font=('Arial', 14))
button_7.grid(row=4, column=1)
button_8 = tk.Button(root, text='8', command=lambda: input_argument('8'), width=5, font=('Arial', 14))
button_8.grid(row=4, column=2)
button_9 = tk.Button(root, text='9', command=lambda: input_argument('9'), width=5, font=('Arial', 14))
button_9.grid(row=4, column=3)
button_0 = tk.Button(root, text='0', command=lambda: input_argument('0'), width=5, font=('Arial', 14))
button_0.grid(row=5, column=2)
# now for all operators and other functions
button_addition = tk.Button(root, text='+', command=lambda: input_argument('+'), width=5, font=('Arial', 14))
button_addition.grid(row=2, column=4)
button_subtraction = tk.Button(root, text='-', command=lambda: input_argument('-'), width=5, font=('Arial', 14))
button_subtraction.grid(row=3, column=4)
button_multiplication = tk.Button(root, text='x', command=lambda: input_argument('*'), width=5, font=('Arial', 14))
button_multiplication.grid(row=4, column=4)
button_division = tk.Button(root, text='/', command=lambda: input_argument('/'), width=5, font=('Arial', 14))
button_division.grid(row=5, column=4)
button_open = tk.Button(root, text='(', command=lambda: input_argument('('), width=5, font=('Arial', 14))
button_open.grid(row=5, column=1)
button_close = tk.Button(root, text=')', command=lambda: input_argument(')'), width=5, font=('Arial', 14))
button_close.grid(row=5, column=3)
# here we can understand when lambda is not necessary
button_equals_to = tk.Button(root, text='=', command=evaluate_argument, width=11, font=('Arial', 14))
button_equals_to.grid(row=6, column=1, columnspan=2)
button_clear = tk.Button(root, text='C', command=clear_argument, width=11, font=('Arial', 14))
button_clear.grid(row=6, column=3, columnspan=2)
# method that runs the window until it's closed
root.mainloop()
