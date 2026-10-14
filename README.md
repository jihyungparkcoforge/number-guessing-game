# number-guessing-game




DEBUG SECRET NUM = 20

## Test Cases

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
