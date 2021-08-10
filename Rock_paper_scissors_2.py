#! /usr/env/python3 import random
import sys

def game():
	rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
	paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
	scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
	ans = int(input("Choose between rock, paper, scissors[0,1,2]: "))
	var = [rock, paper, scissors]
	cp = random.randrange(0,2)
	if ans > 2:
		print("Invalid choice. You lose!")
		sys.exit()
	elif ans == cp:
		print(f"You chose {var[ans]} \n and computer chose{var[cp]}. It's a draw!")
	elif ans < cp:
		print(f"You chose{var[ans]} \n and computer chose{var[cp]}. You lose!")
	elif ans > cp:
		print(f"You chose{var[ans]} \n and computer chose{var[cp]}.You win!")
game()

cont = str(input("Do you want to continue?[y/n]: ")).lower()
while cont == 'y':
	game()
	cont = str(input("Do you want to continue?[y/n]: ")).lower()
if cont == 'n':
	print("Exiting game.")
	sys.exit()
