import tkinter as tk
from tkinter import ttk

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except Exception as e:
        clear_field()
        text_result.insert(1.0, "Error: " + str(e))


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x250")
root.title("Calculator")  # Setting the title of the window

# Use themed widgets for consistent appearance across different platforms
style = ttk.Style()
style.theme_use('clam')  # Use 'clam' theme which is more consistent across platforms

text_result = tk.Text(root, height="2", width=16, font=("Arial", 24))
text_result.grid(row=0, column=0, columnspan=5, sticky="nsew")

buttons = [
    ("1", 2, 1), ("2", 2, 2), ("3", 2, 3),
    ("4", 3, 1), ("5", 3, 2), ("6", 3, 3),
    ("7", 4, 1), ("8", 4, 2), ("9", 4, 3),
    ("0", 5, 2), ("+", 2, 4), ("-", 3, 4),
    ("*", 4, 4), ("/", 5, 4), ("(", 5, 1),
    (")", 5, 3), ("C", 6, 3), ("=", 6, 4),  # corrected '=' to (6, 4)
    (".", 6, 2)
]

for (text, row, column) in buttons:
    if text == "C":
        btn = ttk.Button(root, text=text, width=5, style='my.TButton', command=clear_field)
    elif text == "=":
        btn = ttk.Button(root, text=text, width=5, style='my.TButton', command=evaluate_calculation)
    else:
        btn = ttk.Button(root, text=text, width=5, style='my.TButton', command=lambda t=text: add_to_calculation(t))
    btn.grid(row=row, column=column, sticky="nsew")

# Configure row and column resizing
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()