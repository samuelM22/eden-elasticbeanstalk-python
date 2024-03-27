# Simple Calculator

from tkinter import *

win = Tk()
win.title("Eden Tech Calculator")

#Creating display for results

display = Entry(win, width=45, borderwidth=20)
display.grid(row=0, column=0, columnspan=3)

def eden_button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

def eden_button_clear():
    display.delete(0, END)

def eden_button_addition():
    first_number = display.get()
    global fname
    global operator
    operator = "addition"
    fname = first_number
    display.delete(0, END)

def eden_button_subtraction():
    first_number = display.get()
    global fname
    global operator
    operator = "subtraction"
    fname = first_number
    display.delete(0, END)

def eden_button_multiplication():
    first_number = display.get()
    global fname
    global operator
    operator = "multiplication"
    fname = first_number
    display.delete(0, END)

def eden_button_division():
    first_number = display.get()
    global fname
    global operator
    operator = "division"
    fname = first_number
    display.delete(0, END)

def eden_button_equals():
    second_number = display.get()
    if operator == "addition":
        display.delete(0, END)
        display.insert(0, float(fname) + float(second_number))

    if operator == "subtraction":
        display.delete(0, END)
        display.insert(0, float(fname) - float(second_number))

    if operator == "multiplication":
        display.delete(0, END)
        display.insert(0, float(fname) * float(second_number))

    if operator == "division":
        display.delete(0, END)
        display.insert(0, float(fname) / float(second_number))



#Creating Buttons for Calculator

eden_buttons_one = Button(win, text="1", padx=40, pady=20, command=lambda: eden_button_click(1))
eden_buttons_two = Button(win, text="2", padx=40, pady=20, command=lambda: eden_button_click(2))
eden_buttons_three = Button(win, text="3", padx=40, pady=20, command=lambda: eden_button_click(3))
eden_buttons_four = Button(win, text="4", padx=40, pady=20, command=lambda: eden_button_click(4))
eden_buttons_five = Button(win, text="5", padx=40, pady=20, command=lambda: eden_button_click(5))
eden_buttons_six = Button(win, text="6", padx=40, pady=20, command=lambda: eden_button_click(6))
eden_buttons_seven = Button(win, text="7", padx=40, pady=20, command=lambda: eden_button_click(7))
eden_buttons_eight = Button(win, text="8", padx=40, pady=20, command=lambda: eden_button_click(8))
eden_buttons_nine = Button(win, text="9", padx=40, pady=20, command=lambda: eden_button_click(9))
eden_buttons_zero = Button(win, text="0", padx=40, pady=20, command=lambda: eden_button_click(0))
eden_buttons_add = Button(win, text="+", padx=40, pady=20, command=lambda: eden_button_addition())
eden_buttons_minus = Button(win, text="-", padx=40, pady=20, command=lambda: eden_button_subtraction())
eden_buttons_multiply = Button(win, text="*", padx=40, pady=20, command=lambda: eden_button_multiplication())
eden_buttons_divide = Button(win, text="/", padx=40, pady=20, command=lambda: eden_button_division())
eden_buttons_dot = Button(win, text=".", padx=40, pady=20, command=lambda: eden_button_click("."))
eden_buttons_clr = Button(win, text="C", padx=40, pady=20, command=lambda: eden_button_clear())
eden_buttons_equals = Button(win, text="=", padx=40, pady=20, command=lambda: eden_button_equals())

#Placing the buttons on grids

eden_buttons_seven.grid(row=1, column=0)
eden_buttons_eight.grid(row=1, column=1)
eden_buttons_nine.grid(row=1, column=2)

eden_buttons_four.grid(row=2, column=0)
eden_buttons_five.grid(row=2, column=1)
eden_buttons_six.grid(row=2, column=2)

eden_buttons_one.grid(row=3, column=0)
eden_buttons_two.grid(row=3, column=1)
eden_buttons_three.grid(row=3, column=2)

eden_buttons_add.grid(row=4, column=0)
eden_buttons_zero.grid(row=4, column=1)
eden_buttons_minus.grid(row=4, column=2)

eden_buttons_multiply.grid(row=5, column=0)
eden_buttons_dot.grid(row=5, column=1)
eden_buttons_divide.grid(row=5, column=2)

eden_buttons_equals.grid(row=6, column=0)
eden_buttons_clr.grid(row=6, column=1)

win.mainloop()
