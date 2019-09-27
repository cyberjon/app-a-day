import random

words = ['cat', 'computer','house','desktop','python']




rand_no  = random.randint(0,len(words)-1)

random_word = words[rand_no]

word = "_" * len(random_word)
clue = list(word)

lives=5

user_input = input('I am thinking  of a random word. Would like to play Y/N:')


if user_input.lower() =='n':
    print('Good Bye')
    exit()
elif user_input.lower() =='y':
    print('The numner of letters are: '+str(len(word)))
    
    user_guess =True

while user_guess:
        guess = input("Enter a letter:")
        print(f'You have {lives}')
        

        if guess  in  random_word:
            index = random_word.index(guess)

            print('The letter is  in the word\n')
            clue[index] = guess
            word ="".join(clue)
            print(word)
            
            

        if word == random_word:
                user_guess=False
                print("You guessed right!")
                print("You win")
                print("Good Bye")
                exit()
            

        if guess not in  random_word:
            print('The letter is not in the word\n')
            lives  -= 1

        if lives == 0:
            print("You have use up all you lives\n Goodbye")
            exit()

        
