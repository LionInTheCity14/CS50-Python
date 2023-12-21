import random

min = int(input("What's the minimum range: "))
max = int(input("What's the maximum range: "))
def guess(max=100):
    random_num = random.randint(1, max)
    guess = 0
    cnt = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {max}: "))
        if guess < random_num:
            print("too low")
        elif guess > random_num:
            print("too high")
        else:
            print(f"Yay, congrats. You have guessed the number {random_num} in {cnt} guesses")
        cnt += 1    

def computer_guess(min=1, max=100):
    start, end = min, max
    cnt = 0
    feedback = ""
    while feedback != "c" and start != end:
        guess = random.randint(start, end)
        feedback = str(input(f"Is {guess} too high(H), too low(L) or correct(C) ?? ")).lower()
        if feedback == "h":
            end = guess - 1
        elif feedback == "l":
            start = guess + 1
        cnt += 1
        
    print(f"Yay, The computer guessed your number, {guess}, correctly in {cnt} moves")


guess(max)
computer_guess(min, max)