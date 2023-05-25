import random

max_range = input('Type a number: ')

# Verifying user input is a number and greater than zero.
if max_range.isdigit():
    max_range = int(max_range)

    if max_range <= 0:
        print('Please type a number larger than zero next time.')
        quit()
else:
    print('Please type a number next time.')

# Generating a random number with max_range being inclusive.
random_number = random.randint(0, max_range)

# User guessing and validating user input.
guesses = 0
while True:
    guesses += 1
    user_guess = input('Make a guess: ')

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print('Correct!')
        break
    else:
        print('Try again!')

print('You got it in', guesses, 'guesses.')