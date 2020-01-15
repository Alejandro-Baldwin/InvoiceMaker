def amAdd(time):
    time = time + [' ', 'A', 'M']
    time = ''.join(time)
    return time

def pmAdd(time):
    time = time + [' ', 'P', 'M']
    time = ''.join(time)
    return time

def amToPmDetector(time):
    if time[1] == '2' and time[0] == '1':
        t = pmAdd(time)
        h = int(''.join(time[0:2]))
        return t, h
    else:
        t = amAdd(time)
        h = 24
        return t, h

def pmToAmDetector(time):
    if time[1] == '2' and time[0] == '1':
        t = amAdd(time)
        h = 24
        return t, h
    else:
        t = pmAdd(time)
        h = int(''.join(time[0:2])) + 12
        return t, h

def overNineCheckerAm(time):
    #Checks if the extra hour is it gonna make it go from 9 to 10
    if int(time[1]) < 9:
        time[1] = str(int(time[1]) + 1)
        time[-1] = '0'
        time[-2] = '0'
        #Checks if time goes from 11 AM to 12 PM
        hour = amToPmDetector(time)
        return hour
    #Default Behaviour
    else: 
        time[0] = str(int(time[0]) + 1)
        time[1] = '0'
        time[-1] = '0'
        time[-2] = '0'
        #Checks if time goes from 11AM to 12PM
        hour = amToPmDetector(time)
        return hour

def roundDownAm(time):
    time[-1] = '0'
    time[-2] = '0'
    time = amAdd(time)
    if time[0] == '0':
        h = int(time[1])
        return time, h
    elif time[0] == '1' and time[1] == '2':
        h = 24
        return time, h
    else:
        h = int(''.join(time[0:2]))
        return time, h

def overNineCheckerPm(time):
    #Checks if the extra hour is it gonna make it go from 9 to 10
    if int(time[1]) < 9:
        time[1] = str(int(time[1]) + 1)
        time[-1] = '0'
        time[-2] = '0'
        #Checks if time goes from 11 AM to 12 PM
        hour = pmToAmDetector(time)
        return hour
    #Default Behaviour
    else: 
        time[0] = str(int(time[0]) + 1)
        time[1] = '0'
        time[-1] = '0'
        time[-2] = '0'
        #Checks if time goes from 11AM to 12PM
        hour = pmToAmDetector(time)
        return hour
    
def roundDownPm(time):
    time[-1] = '0'
    time[-2] = '0'
    time = pmAdd(time)
    if time[0] == '0':
        h = int(time[1]) + 12
        return time, h
    elif time[0] == '1' and time[1] == '2':
        h = 12
        return time, h
    else:
        h = int(''.join(time[0:2])) + 12
        return time, h

def time_fixer(hour):
    #hIn is the inputed time in list format
    hIn = list(hour.upper())

    #Check if the input has 00:00, if not add the 00
    if len(hIn) <= 7:
        hIn.insert(0, '0')
        #Check if time is AM
        if 'A' in hIn:
            del hIn[-3:]
            #Check if time is roundable to the next hour
            if int(hIn[-2]) >= 3:
                #Checks if the extra hour is it gonna make it go from 9 to 10
                hour = overNineCheckerAm(hIn)
                return hour
            #If time doesn't round up to next hour, it rounds down
            else:
                hour = roundDownAm(hIn)
                return hour[0], hour[1]
        #Check if time is PM
        else:
            del hIn[-3:]
            #Check if time is roundable to the next hour
            if int(hIn[-2]) >= 3:
                #Checks if the extra hour is it gonna make it go from 9 to 10
                hour = overNineCheckerPm(hIn)
                return hour
            #If time doesn't round up to next hour, it rounds down
            else:
                hour = roundDownPm(hIn)
                return hour[0], hour[1]
    #Checks if time already has 00:00 format and 
    else:
        if 'A' in hIn:
            del hIn[-3:]
            #Check if time is roundable to the next hour
            if int(hIn[-2]) >= 3:
                #Checks if the extra hour is it gonna make it go from 9 to 10
                hour = overNineCheckerAm(hIn)
                return hour
            #If time doesn't round up to next hour, it rounds down
            else:
                hour = roundDownAm(hIn)
                return hour[0], hour[1]
        #Check if time is PM
        else:
            del hIn[-3:]
            #Check if time is roundable to the next hour
            if int(hIn[-2]) >= 3:
                #Checks if the extra hour is it gonna make it go from 9 to 10
                hour = overNineCheckerPm(hIn)
                return hour
            #If time doesn't round up to next hour, it rounds down
            else:
                hour = roundDownPm(hIn)
                return hour[0], hour[1]
