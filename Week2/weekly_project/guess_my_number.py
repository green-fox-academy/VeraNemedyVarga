# Write a program where the program chooses a number between 1 and 100. The player is then asked to enter a guess. If the player guesses wrong, then the program gives feedback and ask to enter an other guess until the guess is correct.
#
# Make the range customizable (ask for it before starting the guessing).
# You can add lives. (optional)

import random
print("Let's play a little number guessing game \n")
start = int(input("Tell me, what should be the lowest guessable number?:  "))
end = int(input("What should be the highest?: "))
print("Guess a number between " + str(start) + " and " + str(end) + ". You have five lives.")

chosen_number = random.randint(start, end)
lives = 5
guessed_number = int(input("Guess my number: "))

while chosen_number != guessed_number:
    if chosen_number > guessed_number:
        print("Pick a higher number")
    elif chosen_number < guessed_number:
         print("Pick a lower number")
    guessed_number = int(input("Take another guess: "))
    lives -= 1
    if chosen_number == guessed_number and lives >= 0:
        print("You guessed it!")
        break
    if lives >= 1:
        print("you have " + str(lives) + " lives left.")
    elif lives == 0:
        print("Game over")
        break
