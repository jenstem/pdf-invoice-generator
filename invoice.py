from tkinter import *

root = Tk()
root.title("Invoice Generator")


# Medicine List
medicines = {
    "Medicine A": 10,
    "Medicine B": 20,
    "Medicine C": 30,
    "Medicine D": 40,
}


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


# Button to add medicine
add_button = Button(root, text="Add Medicine")
add_button.pack()


# Invoice Total
total_amount_label = Label(root, text="Total Amount: ")
total_amount_label.pack()

total_amount_entry = Entry(root)
total_amount_entry.pack()


# Customer
customer_label = Label(root, text="Customer Name: ")
customer_label.pack()

customer_entry = Entry(root)
customer_entry.pack()


# Button to generate invoice
generate_button = Button(root, text="Generate Invoice")
generate_button.pack()


# Invoice Text
invoice_text = Text(root, height=10, width=50)
invoice_text.pack()


root.mainloop()