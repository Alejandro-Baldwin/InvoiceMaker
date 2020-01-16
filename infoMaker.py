from textOnlyValidator import textOnlyValidator
from numberOnlyValidator import numberOnlyValidator
from phoneNumberValidator import phoneNumberValidator

def infoMaker():
    name = textOnlyValidator(input("What's your full Name? : "))
    ssn = phoneNumberValidator(input("What's your SSN? : "))
    client = textOnlyValidator(input("For wich client is this invoice? : "))
    venue = textOnlyValidator(input("What's the venue? : "))
    address = input("What's your address? : ")
    phone = phoneNumberValidator(input("What's your phone number? : "))
    email = input("What's your e-mail? : ").lower()
    invoiceName = phoneNumberValidator(input("What's the invoice number? : "))
    invoiceName = f"{name}'s Invoice {invoiceName}"
    return name, ssn, client, venue, address, phone, email, invoiceName