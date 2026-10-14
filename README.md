# number-guessing-game

Guessing game that runs in the terminal. The computer picks a secret number, and the player guesses it with "too low" and "too high" hints. The player chooses a difficulty level and can play in a timed mode.

## Quick Start

```{shell}
git clone https://github.com/jihyungparkcoforge/number-guessing-game.git
cd number-guessing-game
uv venv
source .venv/bin/activate
python3 guess.py
```

## Mode

|Mode	|Feature	|
|----|----|
|Classic	| No time limit|
|Time Challenge	| 60 second time limit|

## Difficulty levels
|Level	|Range	|Attempts allowed|
|----|----|----|
|Easy	|1 to 50	|10|
|Medium	|1 to 100|	8|
|Hard	|1 to 500	|10|




## Test Cases
DEBUG SECRET NUM = 20
| What I tested | What I did | Expected result | Actual result | Pass
|------------|-----------|--------------|-------------|-----------|
| Too low | Easy, Classic, guess 17 | Shows "Too low" | Too low, remaining attempt: 9 | Yes |
| Too high | Easy. Classic, guess 22 | Shows "Too high" | Too high, remaining attempt: 9 | Yes |
| Correct guess | Easy, Classic, guess 20 | Shows "Congratulations!" | Congratulations! You guessed the number in 1 attempts! | Yes |
| Hit max attempt | Easy, Classic, wrong guess 10 times | Shows "Reach to max attempt" | Reach to max attempt. Secret number was 20 | Yes |
| Invalid above range input guess | Easy, Classic, enter 123 | Shows "Invalid" and ask number again | Invalid. What is your number? between 1 and 50 | Yes |
| Invalid char input guess | Easy, Classic, enter "hi" | Shows "Invalid"and ask number again | Invalid. What is your number? between 1 and 50 | Yes |
| Invalid difficulty choice | Type "easy" instead of number | Shows "Invalid" and ask difficulty again | Invalid input. Choose difficulty level:\n1. Easy\n2. Medium\n3. Hard | Yes|
| Invalid mode choice | Type "classic" instead of number | Shows "Invalid" and ask mode choice again | Invalid input. Choose mode:\n1. Classic\n2. Challenge | Yes |
| Challenge mode time checking when asking guess | Easy, Challenge, guess 17 | Shows "Too low", remaining attempt, ask again with time left | Too low, remaining attempt: 9\nWhat is your number? between 1 and 50\nYou have 56 seconds | Yes |
| Times up | Easy, Challenge, wait more than 60 sec, guess 17 | Shows "Time is up! Secret number was {secret num}" | Time is up! Secret number was 20 | Yes |
