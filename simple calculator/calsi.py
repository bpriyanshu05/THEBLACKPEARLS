from tkinter import *
import math

# Global variables for memory function
memory = 0
expression = ""

# Function to update the input field when a button is pressed
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except ZeroDivisionError:
        equation.set("Cannot divide by zero")
        expression = ""
    except Exception:
        equation.set("Invalid input")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    equation.set("")

# Function to calculate square root
def sqrt():
    try:
        global expression
        total = str(math.sqrt(float(expression)))
        equation.set(total)
        expression = ""
    except ValueError:
        equation.set("Invalid input")
        expression = ""

# Function to calculate exponentiation
def power():
    global expression
    expression += "**"
    equation.set(expression)

# Function to add to memory
def mem_add():
    global memory, expression
    memory += float(equation.get())
    expression = ""
    equation.set("")

# Function to recall memory
def mem_recall():
    global memory
    equation.set(memory)

# Function to clear memory
def mem_clear():
    global memory
    memory = 0

# Creating the main window
gui = Tk()
gui.title("Calculator")

equation = StringVar()

# Create the input field
input_field = Entry(gui, textvariable=equation, font=('Arial', 18), bd=8, insertwidth=2, width=14, borderwidth=4)
input_field.grid(columnspan=4)

# Button configurations
button_config = {'fg': 'black', 'bg': 'red', 'height': 2, 'width': 7, 'font': ('Arial', 12)}

# Define buttons
buttons = [
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('*', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('/', 5, 3),
    ('√', 6, 0), ('^', 6, 1), ('Clear', 6, 2), ('M+', 6, 3),
    ('MR', 7, 0), ('MC', 7, 1)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    action = lambda x=text: press(x) if x not in ['=', 'Clear', '√', '^', 'M+', 'MR', 'MC'] else None
    Button(gui, text=text, command=action, **button_config).grid(row=row, column=col)

# Special buttons
Button(gui, text='=', command=equalpress, **button_config).grid(row=5, column=2)
Button(gui, text='Clear', command=clear, **button_config).grid(row=6, column=2)
Button(gui, text='√', command=sqrt, **button_config).grid(row=6, column=0)
Button(gui, text='^', command=power, **button_config).grid(row=6, column=1)
Button(gui, text='M+', command=mem_add, **button_config).grid(row=6, column=3)
Button(gui, text='MR', command=mem_recall, **button_config).grid(row=7, column=0)
Button(gui, text='MC', command=mem_clear, **button_config).grid(row=7, column=1)

# Start the GUI
gui.mainloop()
