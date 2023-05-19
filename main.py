import random

print("Hello, welcome to the Math test. This tests addition, multiplycation, subtraction, and the power of.")

play = input("Whould you like to play? y or n.")
play.lower()

opporators = ['+', '-', '*', '/', '**']
rounds = 0
i = 1
score = 0

if play == 'y':
    rounds = int(input("How many rounds would you like: "))
    while i <= rounds:
        opp = random.choice(opporators)
        print(opp)
        if opp == '+':
            rand1 = random.randint(1, 100)
            rand2 = random.randint(1, 100)
            playans = int(input(f"What does {rand1} plus {rand2} equal: "))
            if playans == rand1 + rand2:
                print("Correct")
                i += 1
                score += 1
            elif playans != rand1 + rand2:
                print("Incorrect")
                i += 1
        elif opp == '-':
            rand1 = random.randint(1, 100)
            rand2 = random.randint(1, 100)
            playans = int(input(f"What does {rand1} minus {rand2} equal: "))
            if playans == rand1 - rand2:
                print("Correct")
                i += 1
                score += 1
            elif playans != rand1 - rand2:
                print("Incorrect")
                i += 1
        elif opp == '*':
            rand1 = random.randint(1, 20)
            rand2 = random.randint(1, 10)
            playans = int(input(f"What does {rand1} times {rand2} equal: "))
            if playans == rand1 * rand2:
                print("Correct")
                i += 1
                score += 1
            elif playans != rand1 * rand2:
                print("Incorrect")
                i += 1
        elif opp == '/':
            rand1 = random.randint(1, 20)
            rand2 = random.randint(1, 10)
            rand3 = rand1 * rand2
            playans = int(
                input(f"What does {rand3} devided by {rand1} equal: "))
            if playans == rand3 / rand1:
                print("Correct")
                i += 1
                score += 1
            elif playans != rand3 / rand1:
                print("Incorrect")
                i += 1
        elif opp == '**':
            rand1 = random.randint(1, 10)
            rand2 = random.randint(1, 3)
            playans = int(input(f"What does {rand1} raise {rand2} equal: "))
            if playans == rand1 ** rand2:
                print("Correct")
                i += 1
                score += 1
            elif playans != rand1 ** rand2:
                print("Incorrect")
                i += 1

print(f"Your score was {score}.")
if score < rounds / 2:
    print("You lost.")
elif score > rounds / 2:
    print("You won!")
elif score == rounds / 2:
    print("It was a tie.")
