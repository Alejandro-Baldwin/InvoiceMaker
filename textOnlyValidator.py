import string

def textOnlyValidator(text):
    a = string.ascii_letters + ' '
    while True:
        e = []
        while True:
            for i in text:
                if i not in a:
                    e.append(i)
                else:
                    continue
            if len(e) != 0:
                text = input(f"Please input valid text: ('{e[0]}' is not a valid character)" )
                e = []
            else:
                return text