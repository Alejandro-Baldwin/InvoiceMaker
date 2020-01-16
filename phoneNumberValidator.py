import string

def phoneNumberValidator(number):
    n = '0123456789 ()-'
    while True:
        e = []
        while True:
            for i in number:
                if i not in n:
                    e.append(i)
                else:
                    continue
            if len(e) != 0:
                number = input(f"Please input valid phone number: ")
                e = []
            else:
                return number