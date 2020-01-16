import string

def numberOnlyValidator(number):
    n = '0123456789'
    while True:
        e = []
        while True:
            for i in number:
                if i not in n:
                    e.append(i)
                else:
                    continue
            if len(e) != 0:
                number = input(f"Please input valid number: ('{e[0]}' is not a valid character) ")
                e = []
            else:
                return number