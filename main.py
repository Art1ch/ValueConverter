import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Value converter on python tkinter")
root.configure(width=400, height=400, background="gray")


def convert() -> None:
    input_value: float = float(input_value_entry.get())
    first_unit: str = first_unit_string_var.get()
    second_unit: str = second_unit_string_var.get()

    if first_unit == second_unit:
        result_entry.delete(0, END)
        result_entry.insert(0, str(input_value))
        return None

    try:
        result: float = input_value * conversion_rates[(first_unit, second_unit)]
        result_entry.delete(0, END)
        result_entry.insert(0, str(result))
    except KeyError as ex:
        print(ex)
        result_entry.delete(0, END)
        result_entry.insert(0, "You can't match these units")


all_units: tuple = \
    ("Miles", "Kilometers",
     "Pounds", "Kilograms",
     "Inches", "Centimeters",
     )

conversion_rates: dict = \
    {
        ("Miles", "Kilometers"): 1.60934,
        ("Kilometers", "Miles"): 0.621371,
        ("Pounds", "Kilograms"): 0.453592,
        ("Kilograms", "Pounds"): 2.20462,
        ("Inches", "Centimeters"): 2.54,
        ("Centimeters", "Inches"): 0.393701
    }

input_value_label = Label(root, text="Enter value:", font="Arial 14", background="gray")
input_value_label.place(x=25, y=25)

input_value_entry = Entry(root, width=30)
input_value_entry.place(x=130, y=30)

from_label = Label(root, text="From", font="Arial 14", background="gray")
from_label.place(x=25, y=100)

to_label = Label(root, text="To", font="Arial 14", background="gray")
to_label.place(x=25, y=150)

first_unit_string_var = tk.StringVar(root)
first_unit_string_var.set("Kilometers")

first_unit_menu = tk.OptionMenu(root, first_unit_string_var, *all_units)
first_unit_menu.place(x=100, y=100)

second_unit_string_var = tk.StringVar(root)
second_unit_string_var.set("Miles")

second_unit_menu = tk.OptionMenu(root, second_unit_string_var, *all_units)
second_unit_menu.place(x=100, y=145)

result_label = Label(root, text="Result: ", font="Arial 14", background="gray")
result_label.place(x=25, y=225)

result_entry = Entry(root, width=30)
result_entry.place(x=95, y=230)

convert_button = Button(root, text="Convert", font="Arial 14", width=8, command=convert)
convert_button.place(x=140, y=325)

if __name__ == "__main__":
    root.mainloop()
