from tkinter import *

root = Tk()
root.title("Invoice Generator")


# Medicine
medicine_label = Label(root, text="Medicine: ")
medicine_label.pack()

medicine_listbox = Listbox(root, selectmode=SINGLE)
medicine_listbox.pack()


# Quantity
quantity_label = Label(root, text="Quantity: ")
quantity_label.pack()
quantity_entry = Entry(root)
quantity_entry.pack()


# Button
add_button = Button(root, text="Add Medicine")
add_button.pack()


root.mainloop()