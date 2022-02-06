import random

def guess(x):
    random_number = random.randint(1, x)
    g = 0
    while g != random_number:
        g = int(input(f"Enter a number between 1 and {x}: "))
        if g > random_number:
            print("You've gone a bit too high...")
        elif g < random_number:
            print("You've gone a bit too low...")

    print("Yes! That's the correct guess!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            g = random.randint(low, high)
        else:
            g = low
        feedback = input(f"Is {g} too high(H), too low(L) or correct(C)? ").lower()
        if feedback == 'h':
            high = g - 1
        elif feedback == 'l':
            low = g + 1

    print(f"The computer guessed your number {g} correctly!")


computer_guess(10)