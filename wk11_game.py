from random import randint
correct_guess = False
chosen_num = randint(1,100)
guesses = []
valid_guess = False
while not correct_guess:
    while not valid_guess:
        current_guess = input("enter a guess 1 - 100")
        if current_guess.isdigit():
            if (int(current_guess) >=0 and int(current_guess) <= 100):
                valid_guess = True
            else:
                print("out of bounds")
        guesses.append(int(current_guess))
    if (guesses[-1] == chosen_num):
        correct_guess = True
        print(f"you have guessed correctly after {len(guesses)} guesses")
    if  len(guesses) == 1:
        if (abs(chosen_num - guesses[-1]) <= 10):
            print("WARM")
        else:
            print("COLD")
    else:
        if (abs(chosen_num - guesses[-1]) < abs(chosen_num - guesses[-2])):
            print("Warmer")
        else:
            print("Colder")
    valid_guess = False
        
    