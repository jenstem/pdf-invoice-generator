from tkinter import *
from fpdf import FPDF


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
total_amount = 0.0


# Function to add medicine to the invoice
def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR)
    if selected_medicine:
        quantity = int(quantity_entry.get())
        price = medicines[selected_medicine]
        item_total = price * quantity
        invoice_items.append((selected_medicine, quantity, item_total))
        total_amount_entry.delete(0, END)
        total_amount_entry.insert(END, str(calculate_total()))
        update_invoice_text()


# Function to calculate the total amount
def calculate_total():
    total = 0.0
    for item in invoice_items:
        total += item[2]
    return total


# Function to update the invoice text
def update_invoice_text():
    invoice_text.delete(1.0, END)
    for item in invoice_items:
        invoice_text.insert(END, f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n")


# Function to generate the invoice
def generate_invoice():
    customer_name = customer_entry.get()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, text="Big Pharma SBC", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.cell(0, 10, text="123 Main Street", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.cell(0, 10, text="Columbus, OH 43004", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.cell(0, 15, text="", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.cell(0, 10, text="Invoice", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.cell(0, 10, text=f"Customer: {customer_name}", new_x="LMARGIN", new_y="NEXT", align="L")
    pdf.cell(0, 10, text="", new_x="LMARGIN", new_y="NEXT", align="C")

    for item in invoice_items:
        medicine_name, quantity, item_total = item
        pdf.cell(0, 10, text=f"Medicine: {medicine_name}, Quantity: {quantity}, Total: {item_total}", new_x="LMARGIN", new_y="NEXT", align="L")
    pdf.cell(0, 10, text=f"Total Amount:  $" + str(calculate_total()) + "0", new_x="LMARGIN", new_y="NEXT", align="L")

    pdf.output("invoice.pdf")


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
generate_button = Button(root, text="Generate Invoice", command=generate_invoice)
generate_button.pack()


# Invoice Text
invoice_text = Text(root, height=10, width=50)
invoice_text.pack()


root.mainloop()