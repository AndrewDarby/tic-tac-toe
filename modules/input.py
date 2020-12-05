
def user_choice():
    '''
    '''
    print("Position on board is given by letter for Col = a,b,. and digit for Row =1,2,...")
    validinput = False
    while not validinput:
        position = input("Enter position on board; e.g. A1, B3")
        validinput = validate_position(position)
        if not validinput:
            print("First characher must be alpabetic,A,B,C, second char must be numeric digit")

    return [ord(position[0].lower())-96,  int(position[1])]


def validate_position(position):
    return len(position) == 2 and position[1].isdigit() and ord(position[0].lower()) >=97 and ord(position[0].lower()) <=99