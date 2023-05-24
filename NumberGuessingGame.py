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
print(random_number)
