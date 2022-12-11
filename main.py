import images as img
import random

choices = (img.rock,img.paper,img.scissors)

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))
if player < 0 or player > 2:
    print("Player chose an invalid number. Player loses!")
else:
  ai = random.randint(0,2)
  
  print(f"\nPlayer:\n{choices[player]}")
  print(f"\nAI:\n{choices[ai]}\n")
  
  if player == ai:
      print("It's a draw!")
  elif player == 0 and ai == 1:
      print("Paper beats Rock. AI Wins!")
  elif player == 0 and ai == 2:
      print("Rock beats Scissors. Player Wins!")
  elif player == 1 and ai == 0:
      print("Paper beats Rock. Player Wins!")
  elif player == 1 and ai == 2:
      print("Scissors beats Paper. AI Wins!")
  elif player == 2 and ai == 0:
      print("Rock beats Scissors. AI Wins!")
  elif player == 2 and ai == 1:
      print("Scissors beats Paper. Player Wins!")
