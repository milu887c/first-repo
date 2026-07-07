import random


print('===================\nRock Paper Scissors\n===================')
print("Let's play!\n1) Rock '✊'\n2) paper '✋'\n3) scissors '✌️'")

player = int(input('Pick a number: '))

computer = random.randint(1,3)

choices =  ['✊', '✋', '✌️']

print(f"you chose: {choices[player -1]}")
print(f"CPU chose: {choices[computer -1]}")


if player == computer:
    print('DRAW!')
elif player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
    print('The player won!')
else: 
    print('The CPU won!')




