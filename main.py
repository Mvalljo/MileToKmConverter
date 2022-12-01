from tkinter import *

# Create Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=5)

# Create Entry
entry = Entry(width=10, font=("Arial", 15))
entry.grid(column=3, row=0)

# Create Four Texts
label1 = Label(text="Miles", font=("Arial", 15))
label1.grid(column=4, row=0)
label2 = Label(text="is equal to", font=("Arial", 15))
label2.grid(column=2, row=2)
label3 = Label(text="0", font=("Arial", 15))
label3.grid(column=3, row=2)
label4 = Label(text="Km", font=("Arial", 15))
label4.grid(column=4, row=2)


# Create Button
def action():
    miles = float(entry.get())
    km = round(miles * 1.6)
    label3.config(text=km)


button = Button(text="Calculate", font=("Arial", 15), command=action)
button.grid(column=3, row=5)

window.mainloop()
