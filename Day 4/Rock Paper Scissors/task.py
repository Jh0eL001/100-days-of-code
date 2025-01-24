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
import random
game_images = [rock, paper, scissors]
bot_choice = random.randint(0, 2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[player_choice])
print("Computer chose:")
print(game_images[bot_choice])
if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number. You lose!")
elif player_choice == bot_choice:
    print("It's a draw!")
elif (player_choice == 0 and bot_choice == 2) or \
     (player_choice == 1 and bot_choice == 0) or \
     (player_choice == 2 and bot_choice == 1):
    print("You win!")
else:
    print("You lose!")