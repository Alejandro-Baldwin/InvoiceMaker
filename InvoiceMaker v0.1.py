from start import start
from printer import printer
from hourChecker import hourChecker
import pandas as pd
from time_fixer import time_fixer
from date_fixer import date_fixer
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

print("Welcome to your InvoiceMaker 0.1\nLet's start creating an Invoice!!!")
s = start()
name = input("What's your full Name? : ")
ssn = input("What's your SSN? : ")
client = input("For wich client is this invoice? : ")
venue = input("What's the venue? : ")
address = input("What's your address? : ")
phone = input("What's your phone number? : ")
email = input("What's your e-mail? : ").lower()
head = f"Name: {name}\nSSN: {ssn}\nPhone Number: {phone}\nE-mail: {email}\nSend to: {address}\nClient: {client}\nVenue: {venue}\n"
invoiceName = input("What's the invoice number? : ")
invoiceName = f"{name}'s Invoice {invoiceName}"
info = {'info':[name,ssn,client,venue,address,phone,email], 'fields':['Name: ', 'SSN: ', 'Client:', 'Venue: ', 'Address: ', 'Phone: ', 'E-mail: ']}


while s == True:
    newLine = "Y"
    lines = []
    dateList = []
    positionList = []
    timeInList = []
    timeOutList = []
    walkAwayList = []
    rateList = []
    hoursList = []
    otList = []
    totalList = []
    grandTotal = 0
    while newLine == "Y":
        date = input("For what date do you want to create this Invoice? (mm/dd/yy) : ")
        position = input("What's your position for this day? : ").capitalize()
        timeIn = input("At what time did you got in? (AM/PM) : ").upper()
        timeOut = input("At what time did you got out? (AM/PM) : ").upper()
        walkAway = input("Did you have an hour of Walkaway? (Y/N) : ").upper()
        rate = input("What's your rate for this position? (Only numbers) : ")
        body = printer(date, position, timeIn, timeOut, walkAway, rate)
        lines.append(body[0])
        grandTotal += body[2]
        dateK = date_fixer(date)
        dateList.append(dateK)
        positionList.append(position)
        timeInList.append(time_fixer(timeIn)[0])
        timeOutList.append(time_fixer(timeOut)[0])
        #Gets the time fixed and gets the number for total time logic
        inh = time_fixer(timeIn)
        outh = time_fixer(timeOut)
        #Calculate the total amount of hours
        hours = outh[1] - inh[1]
        ot = 0
        timeH = hourChecker(hours, walkAway)
        hours = timeH[0]
        ot = timeH[1]
        hoursList.append(str(hours))
        walkAwayList.append(walkAway)
        otList.append(str(ot))
        rateList.append(f'${rate}')
        total = (hours * int(rate)) + (ot * (int(rate) * 1.5))
        totalList.append(str(total))
        newLine = body[1]
    else:
        gT = len(rateList) + 11
        grandT = {'field':['Grand Total: '],'total':[str(grandTotal)]}
        path = f'{invoiceName}.xlsx'
        xldata = {'Date':dateList,'Position':positionList,'Time In:':timeInList,'Time Out:':timeOutList, 'Walkaway:':walkAwayList, 'Hours:':hoursList, 'OT:':otList, 'Rate:':rateList, 'Total:':totalList}
        df2 = pd.DataFrame(info)
        df2.set_index('fields', drop=True, inplace=True)
        df = pd.DataFrame(data = xldata)
        df3 = pd.DataFrame(grandT)
        df3.set_index('field', drop=True, inplace=True)
        writer = ExcelWriter(path, engine ='xlsxwriter', mode = 'w')
        df2.to_excel(writer, header=None)
        df3.to_excel(writer, startcol=7, startrow=gT, header=None)
        df.to_excel(writer, index=False, startrow=10)
        writer.save() 
        print("Thanks for using InvoiceMaker v0.1")
        break