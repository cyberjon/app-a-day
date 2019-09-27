#Word guess game 
import random

words = ['cat', 'computer', 'house','desktop','python']



rand_no  = random.randint(0,len(words))

random_word = words[rand_no]

lives=5

user_input = input('I am thinking  of a random word. Would like to play Y/N:')

if user_input.lower() =='n':
    print('Good Bye')
    exit()
elif user_input.lower() =='y':
    
    user_guess =True
    
    while user_guess:
        guess = input("Enter a Guess:")
        print(f'You have {lives}')

        if guess != random_word:
            lives  -= 1

        if lives == 0:
            print("You have use up all you lives\n Goodbye")
            exit()
           

        if guess == random_word:
            user_guess=False
            print("You guessed right!")
            print("You win")
            print("Good Bye")
            exit()
        


            
