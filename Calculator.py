import random
import tkinter as tk
import math as m
import time
def log(a, b=10):
    return m.log(a, b)
def update_text_widget():
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, argument)
    text_result.mark_set("insert", f"1.{cursor_position}")
def input_argument(button_input):
    global argument, cursor_position
    argument = argument[:cursor_position] + str(button_input) + argument[cursor_position:]
    cursor_position += len(button_input)
    update_text_widget()
def del_argument():
    global argument, cursor_position
    # checks if cursor is at the start
    # if not, it deletes the character to the left of the cursor, and adjusts cursor position accordingly
    if cursor_position > 0:
        argument = argument[:cursor_position-1] + argument[cursor_position:]
        cursor_position -= 1
        update_text_widget()
def move_cursor_left():
    global cursor_position
    if cursor_position > 0:
        cursor_position -= 1
        update_text_widget()
def move_cursor_right():
    global cursor_position
    if cursor_position < len(argument):
        cursor_position += 1
        update_text_widget()
def clear_argument():
    global argument, cursor_position
    argument = ''
    cursor_position = 0
    update_text_widget()
def evaluate_argument():
    global argument, cursor_position
    try:
        result = str(eval(argument))
        argument = result
        cursor_position = len(argument)
        update_text_widget()
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
def generate_random_hex_color():
    hex_digits = "0123456789ABCDEF"
    color = "#"
    for _ in range(6):
        color += random.choice(hex_digits)
    return color
def randomize_color():
    global root
    for button in root.winfo_children():
        if isinstance(button, tk.Button):
            button.config(bg=generate_random_hex_color(), fg=generate_random_hex_color())
    root.config(bg=generate_random_hex_color())
    text_result.config(bg=generate_random_hex_color(), fg=generate_random_hex_color(), insertbackground=generate_random_hex_color())
# broken, causes calculator to stop responding
def toggle_random():
    global random_is_on
    while random_is_on:
        randomize_color()
        time.sleep(0.15)
    random_is_on = not random_is_on
def randomize_color_uniform():
    global root
    new_color = generate_random_hex_color()
    new_color2 = generate_random_hex_color()
    for button in root.winfo_children():
        if isinstance(button, tk.Button):
            button.config(bg=new_color, fg=new_color2)
    root.config(bg=new_color)
    text_result.config(bg=new_color, fg=new_color2, insertbackground=new_color2)
def regular_color():
    global root
    global button_colour
    global bg_colour
    global text_bg_colour
    global button_text_colour
    global text_colour
    global text_cursor_color
    for button in root.winfo_children():
        if isinstance(button, tk.Button):
            button.config(bg=button_colour, fg=button_text_colour)
    root.config(bg=bg_colour)
    text_result.config(bg=text_bg_colour, fg=text_colour, insertbackground=text_cursor_color)
def empty():
    pass


random_is_on = False
argument = ''
cursor_position = 0

# creates main window or 'root'
root = tk.Tk()
root.title('Calculadora Cientifica')
root.geometry('814x535')

# default colors
bg_colour = "#2c2d32"
text_bg_colour = "#263437"
text_colour = "#7ecccc"
text_cursor_color = "#67a8a8"
button_colour = "#1b4b4b"
button_text_colour = "#3da8a8"

# creates text widget
text_result = tk.Text(root, height=2, width=30, font=('Arial', 36), fg="white")
text_result.grid(columnspan=1000)

# creates all individual button widgets
button_1 = tk.Button(root, text='1', command=lambda: input_argument('1'), width=5, font=('Arial', 14))
button_1.grid(row=2, column=1)
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

button_addition = tk.Button(root, text='+', command=lambda: input_argument('+'), width=5, font=('Arial', 14))
button_addition.grid(row=2, column=4)
button_delete = tk.Button(root, text='Del.', command=del_argument, width=5, font=('Arial', 14))
button_delete.grid(row=2, column=5)
button_subtraction = tk.Button(root, text='-', command=lambda: input_argument('-'), width=5, font=('Arial', 14))
button_subtraction.grid(row=3, column=4)
button_multiplication = tk.Button(root, text='x', command=lambda: input_argument('*'), width=5, font=('Arial', 14))
button_multiplication.grid(row=4, column=4)
button_division = tk.Button(root, text='/', command=lambda: input_argument('/'), width=5, font=('Arial', 14))
button_division.grid(row=5, column=4)
button_dot = tk.Button(root, text='.', command=lambda: input_argument('.'), width=5, font=('Arial', 14))
button_dot.grid(row=5, column=5)
button_open = tk.Button(root, text='(', command=lambda: input_argument('('), width=5, font=('Arial', 14))
button_open.grid(row=5, column=1)
button_close = tk.Button(root, text=')', command=lambda: input_argument(')'), width=5, font=('Arial', 14))
button_close.grid(row=5, column=3)
button_equals_to = tk.Button(root, text='=', command=evaluate_argument, width=11, font=('Arial', 14))
button_equals_to.grid(row=6, column=1, columnspan=2)
button_clear = tk.Button(root, text='C', command=clear_argument, width=11, font=('Arial', 14))
button_clear.grid(row=6, column=3, columnspan=2)
button_random_S = tk.Button(root, text='Rand. Sort.', command=randomize_color, width=11, font=('Arial', 14))
button_random_S.grid(row=10, column=1, columnspan=2)
button_random_U = tk.Button(root, text='Rand. Unif.', command=randomize_color_uniform, width=11, font=('Arial', 14))
button_random_U.grid(row=10, column=3, columnspan=2)
button_regular = tk.Button(root, text='Regular Clr.', command=regular_color, width=11, font=('Arial', 14))
button_regular.grid(row=3, column=5, columnspan=2)
button_log = tk.Button(root, text='log(x)', command=lambda: input_argument('log(x, base)'), width=5, font=('Arial', 14))
button_log.grid(row=3, column=7)
button_e = tk.Button(root, text='e', command=lambda: input_argument('(m.e)'), width=5, font=('Arial', 14))
button_e.grid(row=4, column=5)
button_pi = tk.Button(root, text='π', command=lambda: input_argument('(m.pi)'), width=5, font=('Arial', 14))
button_pi.grid(row=4, column=6)

button_empty_4 = tk.Button(root, text='^', command=lambda: input_argument('**'), width=5, font=('Arial', 14))
button_empty_4.grid(row=4, column=7)

button_left = tk.Button(root, text='<-', command=move_cursor_left, width=5, font=('Arial', 14))
button_left.grid(row=2, column=6)
button_right = tk.Button(root, text='->', command=move_cursor_right, width=5, font=('Arial', 14))
button_right.grid(row=2, column=7)

regular_color()
text_result.focus_set()

root.mainloop()
