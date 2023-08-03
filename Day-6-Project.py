from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.689)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_input.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
miles_input.grid(column=0, row=1)

km_result_label = Label(text="Km")
miles_input.grid(column=1, row=1)

calc_button = Button(text="Calculate", command=miles_to_km)
miles_input.grid(column=1, row=2)

window.mainloop()
