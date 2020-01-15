def hourChecker(hours, walkAway):
    if walkAway == 'Y':
        hours += -1
        if hours > 10:
            ot = hours - 10
            hours = 10
            return hours, ot
        elif hours <= 5:
            hours = 5
            ot = 0
            return hours, ot
        else:
            hours = 10
            ot = 0
            return hours, ot
    else:
        if hours > 10:
            ot = hours - 10
            hours = 10
            return hours, ot
        elif hours <= 5:
            hours = 5
            ot = 0
            return hours, ot
        else:
            hours = 10
            ot = 0
            return hours, ot