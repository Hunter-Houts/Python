import random
import time
level = 0
def main():

    number = random.randint(1,100)

    
    def welcome():
         print('welcome to level ' + str(level + 1) + '!')

    def tryAgain():
        try_again = input('Would you like to play again? (Yes/No): ').lower()
        if try_again.startswith('y'):
            main()
        else:
            print('Alright, Goodbye!')
            time.sleep(3)
            quit()
    def guessing_game(numOfguess):
        guess = 0
        print('You get ' + str(numOfguess) + ' guesses!') 
        while guess < numOfguess:
            user_guess = int(input('Guess a number between 1 and 100: '))
            guess += 1
            if user_guess < number:
                print('Higher')
            elif user_guess > number:
                print('Lower')
            elif user_guess == number:
                print('Congrates, the number was ' + str(number) + '!')
                time.sleep(3)
                print('You won!')
                global level
                level += 1
                tryAgain()
                break
        if guess == numOfguess:
            print('Sorry you ran out of guesses!')
            tryAgain()
    
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
        print('Congrates you beat all the levels!')
        quit()
        
        
        
main()

    
        
