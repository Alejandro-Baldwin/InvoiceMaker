from InvoiceMakekMain import newInvoiceMaker
from InvoiceMakekMain import infoEditor
import os.path

def desicionMaker():    
    action = input("Hey, welcome to your InvoiceMaker v0.2\nWhat would you like to do? (Create/Edit) ").capitalize
    while True:
        if action != 'Create' or action != 'Edit':
            action = input("Please select a valid option! ")
        else:
            return action
    
action = desicionMaker()
if action == "Create":
    newInvoiceMaker()
else:
    name = input("Please enter your full name")
    invoice = input("Wich Invoice do you want to edit, enter Invoice Number: ")
    invoice = f"{name}'s Invoice {invoice}"
    while True:
        if os.path.isfile(invoice):
            infoEditor(invoice)
        else:
            invoice = input("File doesn't exist. Please enter an existing Invoice Number: ")
            invoice = f"{name}'s Invoice {invoice}"