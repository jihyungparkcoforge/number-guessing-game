import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

while True:
    diff = input("Choose difficulty level: Easy, Medium, Hard\n")
    diff = diff.strip().lower()
    if diff in ["easy", "medium", "hard"]:
        break
    else:
        print("Please choose from Easy, Medium, or Hard\n")

if diff == "easy":
    max = 50
    allow = 10
elif diff == "medium":
    max = 100
    allow = 8
else:
    max = 500
    allow = 10

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.




# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
#
if DEBUG_SECRET is not None:
    secretNum = DEBUG_SECRET
else:
    secretNum = random.randint(1, max)

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.
while True:
    guess = input(f"what is your number? between 1 and {max}\n")
    if guess.isdigit():
        guess = int(guess)
        break

current = 1
while guess != secretNum:

    if current == allow:
        print(f"you failed. Secret number was {secretNum}")
        exit(0)

    if guess > secretNum:
        print(f"too high, remaining attempt: {allow-current}")
    else:
        print(f"too low, remaining attempt: {allow-current}")

    while True:
        guess = input(f"what is your number? between 1 and {max}\n")
        if guess.isdigit():
            guess = int(guess)
            break

    current += 1

print("congrat")

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.
