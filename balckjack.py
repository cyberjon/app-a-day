import random

player = random.randint(1,20)
computer = random.randint(1,20)

computer = random.randint(1,20)
black_jack =21

choice = input("Do you want another card:N/Y:").lower()

if choice == 'y':
    player = player + random.randint(1,20)

    if player > black_jack:
        print(f"Player:{player}\nComputer {computer}:\nYou lose")
    if player <= black_jack and player > computer:
        print(f"Player:{player}\nComputer {computer}:\nYou win")
    if player <= black_jack and player < computer:
        print(f"Player:{player}\nComputer {computer}:\nYou lose")
if choice=='n':
    if player > black_jack:
        print(f"Player:{player}\nComputer {computer}:\nYou lose")
    if player <= black_jack and player > computer:
        print(f"Player:{player}\nComputer {computer}:\nYou win")
    if player <= black_jack and player < computer:
        print(f"Player:{player}\nComputer {computer}:\nYou lose")
