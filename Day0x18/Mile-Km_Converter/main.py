# This program converts mile to Kilometer and vice versa
# It has GUI implemented using tkinter

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=50)

input_box = Entry(width=10)
input_box.focus()
input_box.place(x=100, y=30)

first_label = Label(text="Miles", font=("Arial", 12))
first_label.place(x=200, y=30)

phrase_label = Label(text="is equal to ", font=("Arial", 12))
phrase_label.place(x=50, y=60)

km_value = Label(text="      ", font=("Arial", 12))
km_value.place(x=150, y=60)

second_label = Label(text="Km", font=("Arial", 12))
second_label.place(x=200, y=60)


def calculate():
    if radio_state.get() == 2:
        km_value.config(text=(int(input_box.get()) / 1.6))
    else:
        km_value.config(text=(int(input_box.get()) * 1.6))


button = Button(text="Calculate", command=calculate)

button.place(x=150, y=90)


def select_conversion():
    if radio_state.get() == 1:
        first_label.config(text="Miles")
        second_label.config(text="Km")
    else:
        first_label.config(text="Km")
        second_label.config(text="Miles")


radio_state = IntVar()

radiobutton1 = Radiobutton(text="Miles", value=1, variable=radio_state, command=select_conversion)
radiobutton2 = Radiobutton(text="kilometer", value=2, variable=radio_state, command=select_conversion)

radiobutton1.place(x=50, y=150)
radiobutton2.place(x=150, y=150)
