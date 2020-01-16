def monthFixer(date):
    if date[0] != '0':
        date = '0' + date
        return date
    else:
        return date

def monthChecker(date):
    while True:
        date = monthFixer(date)
        if date[2] != '/':  
            date = input('Please input a valid date format: ')
        else:
            return date

def dayFixer(date):
    date = list(date)
    if date[3] != '0':
        date.insert(3, '0')
        date = ''.join(date)
        return date
    else:
        date = ''.join(date)
        return date

def dayChecker(date):
    while True:
        date = dayFixer(date)
        if date[5] != '/':
            date = input('Please input a valid date format:')
        else:
            return date


def yearFixer(date):
    date = date.split('/')
    year = list(date[2])
    if len(year) == 4:
        date = '/'.join(date)
        return date
    elif len(year) == 2:
        date[2] = '20' + date[2]
        date = '/'.join(date)
        return date
    elif len(year) == 1:
        date[2] = '200' + date[2]
        date = '/'.join(date)
        return date

def yearChecker(date):
    while True:
        date = yearFixer(date)
        l = date.split('/')[2]
        if len(l) != 4:
            date = input('Please input a valid date format (mm/dd/yy): ')
        else:
            return date
        
        
def dateValidator(date):
    j = len(date)
    a = "'abcdefghijklmnopqrstuwxyz.,;+][{]}-@#$%^&*()_<>:"
    while True:
        if date in a:
            date = input('Please input a valid date format (mm/dd/yy): ')
        elif j != 10 and date not in a:
            date = monthChecker(date)
            date = dayChecker(date)
            date = yearChecker(date)
            j = len(date)
        else:
            return date