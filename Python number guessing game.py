import random
import time

level = 0


def main():
    number = random.randint(1, 100)

    def welcome():
        print('welcome to level ' + str(level + 1) + '!')

    def try_again():
        again = input('Would you like to play again? (Yes/No): ').lower()
        if again.startswith('y'):
            main()
        else:
            print('Alright, Goodbye!')
            time.sleep(3)
            quit()

    def guessing_game(num_of_guess):
        guess = 0
        print('You get ' + str(num_of_guess) + ' guesses!')
        while guess < num_of_guess:
            user_guess = int(input('Guess a number between 1 and 100: '))
            guess += 1
            if user_guess < number:
                print('Higher')
            elif user_guess > number:
                print('Lower')
            elif user_guess == number:
                print('Congrats, the number was ' + str(number) + '!')
                time.sleep(3)
                print('You won!')
                global level
                level += 1
                try_again()
                break
        if guess == num_of_guess:
            print('Sorry you ran out of guesses!')
            try_again()

        else:
            print('No idea what just happened')

    if level == 0:
        welcome()
        guessing_game(10)
    elif level == 1:
        welcome()
        guessing_game(8)
    elif level == 2:
        welcome()
        guessing_game(6)
    elif level == 3:
        welcome()
        guessing_game(4)
    elif level == 4:
        welcome()
        guessing_game(2)
    elif level == 5:
        print('Congrats you beat all the levels!')
        quit()


if __name__ == '__main__':
    main()
