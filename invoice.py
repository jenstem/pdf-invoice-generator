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


# Shopping cart
invoice_items = []


def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR)
    quantity = int(quantity_entry.get())
    price = medicines[selected_medicine]
    item_total = quantity * price
    invoice_items.append((selected_medicine, quantity, item_total))


# Medicine
medicine_label = Label(root, text="Medicine: ")
medicine_label.pack()

medicine_listbox = Listbox(root, selectmode=SINGLE)
for medicine in medicines:
    medicine_listbox.insert(END, medicine)
medicine_listbox.pack()


# Quantity
quantity_label = Label(root, text="Quantity: ")
quantity_label.pack()
quantity_entry = Entry(root)
quantity_entry.pack()


# Button to add medicine
add_button = Button(root, text="Add Medicine", command=add_medicine)
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