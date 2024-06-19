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
input_field = Entry(gui, textvariable=equation)
input_field.grid(columnspan=4, ipadx=70)

# Define buttons
button1 = Button(gui, text=' 1 ', fg='black', bg='red', command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = Button(gui, text=' 2 ', fg='black', bg='red', command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = Button(gui, text=' 3 ', fg='black', bg='red', command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = Button(gui, text=' 4 ', fg='black', bg='red', command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)

button5 = Button(gui, text=' 5 ', fg='black', bg='red', command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = Button(gui, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = Button(gui, text=' 7 ', fg='black', bg='red', command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = Button(gui, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = Button(gui, text=' 9 ', fg='black', bg='red', command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = Button(gui, text=' 0 ', fg='black', bg='red', command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)

plus = Button(gui, text=' + ', fg='black', bg='red', command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = Button(gui, text=' - ', fg='black', bg='red', command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = Button(gui, text=' * ', fg='black', bg='red', command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = Button(gui, text=' / ', fg='black', bg='red', command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)

equal = Button(gui, text=' = ', fg='black', bg='red', command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)

clear = Button(gui, text='Clear', fg='black', bg='red', command=clear, height=1, width=7)
clear.grid(row=5, column=1)

Decimal = Button(gui, text='.', fg='black', bg='red', command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=6, column=0)

sqrt_button = Button(gui, text=' √ ', fg='black', bg='red', command=sqrt, height=1, width=7)
sqrt_button.grid(row=6, column=1)

power_button = Button(gui, text=' ^ ', fg='black', bg='red', command=power, height=1, width=7)
power_button.grid(row=6, column=2)

mem_add_button = Button(gui, text='M+', fg='black', bg='red', command=mem_add, height=1, width=7)
mem_add_button.grid(row=6, column=3)

mem_recall_button = Button(gui, text='MR', fg='black', bg='red', command=mem_recall, height=1, width=7)
mem_recall_button.grid(row=7, column=0)

mem_clear_button = Button(gui, text='MC', fg='black', bg='red', command=mem_clear, height=1, width=7)
mem_clear_button.grid(row=7, column=1)

# Start the GUI
gui.mainloop()
