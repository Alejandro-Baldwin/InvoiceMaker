from time_fixer import time_fixer
from date_fixer import date_fixer


def printer(date, position, timeIn, timeOut, walkaway, rate):
    date = date_fixer(date)
    #Gets the time fixed and gets the number for total time logic
    inh = time_fixer(timeIn)
    outh = time_fixer(timeOut)
    #Calculate the total amount of hours
    hours = outh[1] - inh[1]
    ot = 0
    if walkaway == 'Y':
        hours += -1
        if hours > 10:
            ot = hours - 10
            hours = 10
        elif hours <= 5:
            hours = 5
        else:
            hours = 10
    else:
        if hours > 10:
            ot = hours - 10
            hours = 10
        elif hours <= 5:
            hours = 5
        else:
            hours = 10
    #Total amount of money
    totalLine = (hours * int(rate)) + (ot * (int(rate) * 1.5))
    body = f"| Date: {date} | Position: {position} | Time In: {inh[0]} | Time Out: {outh[0]} | Walk Away: {walkaway} | Hours: {str(hours)} | OT : {str(ot)} | Rate: ${rate} | Total: ${str(totalLine)} |\n"
    newLine = input("Do you want to create a new Line (Y/N) : ").upper()
    return body, newLine, totalLine
            