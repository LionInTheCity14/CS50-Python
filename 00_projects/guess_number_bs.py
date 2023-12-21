import random

min_range = int(input("What's the minimum range: "))
max_range = int(input("What's the maximum range: "))
def guessNum(min_range=1, max_range=100):
    if min_range > max_range:
        print(f"Invalid input, minimum range can't be greater than maximum range")
        return
    random_num = random.randint(min_range, max_range)
    guess = 0
    cnt = 0
    start, end = 1, max_range
    while guess !=  random_num:
        mid = start + (end - start) // 2
        if mid < random_num:
            start = mid + 1
        elif mid > random_num:
            end = mid - 1
        else:
            print(f"Yay, congrats!, you guessed {random_num} in {cnt} guesses")
            return
        cnt += 1

guessNum(min_range, max_range)