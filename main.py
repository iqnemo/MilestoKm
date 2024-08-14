from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize()
window.config(padx=25,pady=15)

label = Label(text="")
label.grid(column=1, row=1)
label.config(padx=20, pady=20)

label2 = Label(text="is equal to")
label2.grid(column=1, row=2)


entry = Entry(width=5)
entry.insert(END, "0")
entry.grid(column=2, row=1)


label3 = Label(text="Miles")
label3.grid(column=3, row=1)


def conversion():
    value =  round(float(entry.get()) * 1.60934, 3)
    label4.config(text=value)


label4 = Label(text="0")
label4.grid(column=2, row=2)

label5 = Label(text="km")
label5.grid(column=3, row=2)

button = Button(text="Calculate", command=conversion)
button.grid(column=2, row=3)

window.mainloop()