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
    diff = diff.lower()
    if diff in ["easy", "medium", "hard"]:
        break
    else:
        print("Please choose from Easy, Medium, or Hard\n")

if diff == "easy":
    max = 50
elif diff == "medium":
    max = 100
else:
    max = 500

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.

secretNum = random.randint(1, max)


# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.
guess = int(input(f"what is your number? between 1 and {max}\n"))
while guess != secretNum:
    if guess > secretNum:
        print("too high")
    else:
        print("too low")
    guess = int(input("what is your number?\n"))

print("congrat")

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.
