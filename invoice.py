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


# Function to add medicine to the invoice
def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR)
    quantity = int(quantity_entry.get())
    price = medicines[selected_medicine]
    item_total = quantity * price
    invoice_items.append((selected_medicine, quantity, item_total))
    update_invoice_text()


# Function to calculate the total amount
def calculate_total():
    total_amount = 0
    for item in invoice_items:
        total = total + item[2]
    return total


# Function to update the invoice text
def update_invoice_text():
    invoice_text.delete(1.0, END)
    for item in invoice_items:
        invoice_text.insert(END, f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n")


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