import random

num_digits = 3
max_guesses = 10


def main():
    print(f"""'Psyche' is a deductive logic game where you must guess a number based on clues.

    I am thinking of a {num_digits}-digit number with no repeated digits.
    Try to guess what it is.  Here are some clues:
    When I say:     That means:
    Hades           One digit is correct, but is in the wrong position.
    Zeus            One digit is correct, and is in the correct position.
    Cronus          No digits are correct.

    For example, if the secret number was 248 and your guess was 843,
    the clues would be Zeus Hades.""")

    while True:  # Main game loop
        # This stores the secret number the player needs to guess:
        secret_num = getsecret_num()
        print("I have thought up a number...")
        print(f"You have {max_guesses} guesses to get it.")

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ''
            # Keeps looping until they enter a valid guess
            while True:
                print(f"Guess #{num_guesses}:")
                try:
                    guess = input('>')
                    int(guess)  # Attempt to convert guess to an integer
                except ValueError:
                    print("Invalid guess. Please enter a numeric guess.")
                    continue
                if len(guess) != num_digits:
                    print(f"Invalid guess. Please enter a guess with {num_digits} digits.")
                    continue
                break  # Break out of the inner loop if a valid guess is entered

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # They are correct, so break out of the loop
            if num_guesses > max_guesses:
                print("You ran out of guesses")
                print(f"The answer was {secret_num}.")

        # Ask if player wants to play again
        print("Do you want to play again? (yes or no)")
        if not input('>').lower().startswith('y'):
            break
    print("Well done, Hercules. Thanks for playing!")


def getsecret_num():
    """Returns a string made up of num_digits unique random digits."""
    numbers = random.sample('0123456789', num_digits)
    secret_num = ''.join(numbers)
    return secret_num


def get_clues(guess, secret_num):
    """Returns a string with the Hades, Zeus, Cronus clues
    for a guess and a secret number pair."""
    if guess == secret_num:
        return 'You must have struck a deal with the goddess Tyche - You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place
            clues.append('Zeus')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place
            clues.append('Hades')
    if len(clues) == 0:
        return 'Cronus'  # There are no correct digits at all
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


if __name__ == '__main__':
    main()