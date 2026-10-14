###
#number guessing game that runs in the terminal.
#The computer picks a secret number, and the player guesses it with "too low" and "too high" hints.
#The player chooses a difficulty level and can play in a timed mode.
###

import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds attempts_alloweded in Time Challenge mode



print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

# User choose game difficulty level from given 3 options. Type checker applied after it stip empty character before and after, and make it lower case.
# Ask again if it is failed on type checker.
while True:
    diff = input("Choose difficulty level: \n1. Easy\n2. Medium\n3. Hard\n").strip()
    if diff in ["1", "2", "3"]:
        diff = int(diff)
        break
    else:
        print("Invalid input. ", end="")



# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.

# User choose game mode from given 2 options. Type checker applied after it stip empty character before and after, and make it lower case.
# Ask again if it is failed on type checker.
while True:
    mode = input("Choose mode: \n1. Classic\n2. Challenge\n").strip()
    if mode in ["1", "2"]:
        mode = int(mode)
        break
    else:
        print("Invalid input. ", end="")



# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
#
if DEBUG_SECRET is not None:
    secretNum = DEBUG_SECRET
else:
    secretNum = random.randint(1, max)


# asign each variable based on user choice.
if diff == 1:
    maximum_number = 50
    attempts_allowed = 10
elif diff == 2:
    maximum_number = 100
    attempts_allowed = 8
else:
    maximum_number = 500
    attempts_allowed = 10

#Get random integer.
if DEBUG_SECRET is not None:
    secret_number = DEBUG_SECRET
else:
    secret_number = random.randint(1, maximum_number)

#Set start time.
start_time = time.time()

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

num_attempt = 0
while num_attempt < attempts_allowed:

    # Ask number guess until user enter valid input. Number must be integer and must be in an allowed range. Shows remain time and check when mode == 2
    while True:
        if mode == 1:
            guess = input(f"What is your number? between 1 and {maximum_number}\n")
        else:
            guess = input(f"What is your number? between 1 and {maximum_number}\nYou have {int(TIME_LIMIT - (time.time()- start_time))} seconds\n")
        # After a valid guess, the game checks the clock. If time has run out, the game ends and reveals the number, even if that guess was correct.
        if time.time() - start_time > TIME_LIMIT and mode == 2:
            print(f"Time is up! Secret number was {secret_number}")
            exit(0)

        if guess.isdigit() and int(guess) >= 1 and int(guess) <= maximum_number:
            guess = int(guess)
            break
        else:
            print("\nInvalid. ", end="")

    num_attempt += 1

    # exit with attempts when user makes correct guess
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {num_attempt} attempts!")
        exit(0)

    # Give hint
    if guess > secret_number:
        print(f"Too high, remaining attempt: {attempts_allowed-num_attempt}")
    else:
        print(f"Too low, remaining attempt: {attempts_allowed-num_attempt}")

print(f"Reach to max attempt. Secret number was {secret_number}")
