#Ask if you want to create a Invoice. If not, it will kill the script
def start():
    decide = input("Do you want to create an Invoice? (Y/N) : ").upper()
    return decide == "Y"