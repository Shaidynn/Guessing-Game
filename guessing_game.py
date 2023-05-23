import random

MAX_ATTEMPTS = 5

def get_user_guess():
    while True:
        try:
            guess = int(input('Guess your number: '))
            return guess
        except ValueError:
            print('Invalid input. Please enter a valid number.')

def play_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        guess = get_user_guess()

        if secret_number > guess:
            print('Higher...')
        elif secret_number < guess:
            print('Lower...')
        else:
            print('You guessed it! The secret number was', secret_number)
            print('You guessed it in', attempts + 1, 'attempt' if attempts == 0 else 'attempts')
            return

        attempts += 1

    print('Sorry, you are out of tries')
    print('The secret number was', secret_number)

def play_again():
    while True:
        choice = input('Do you want to play again? (y/n): ').lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('Invalid input. Please enter either "y" or "n".')

def main():
    print('Welcome to the Number Guessing Game!')
    print('I will pick a secret number between 1 and 10.')
    print('You have', MAX_ATTEMPTS, 'attempts to guess the number.')
    print('Let\'s begin!')

    while True:
        play_game()
        if not play_again():
            break

    print('Thank you for playing. Goodbye!')

if __name__ == '__main__':
    main()
