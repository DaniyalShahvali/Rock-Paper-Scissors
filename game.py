import random

def greeting():
  print("Hello and Welcome to Rock, Paper and Scissors GAME!")
  user_name = input("What's your name? ")
  print(f"Nice to meet you {user_name}, I hope you have a good GAME!")
  return user_name

def player_move():
  player_choice = input("Please choose Rock, Paper or Scissors: (R/P/S) ").lower()
  return player_choice
def computer_move():
  computer_choice = random.choice(['R', 'P', 'S']).lower()
  return computer_choice

def play_game():
  user_name = greeting()

  player_score = 0
  computer_score = 0

  while True:
    player_choice = player_move()
    computer_choice = computer_move()
    if player_choice == "r" and computer_choice == "p":
      print("You lost! Paper beats Rock.")
      computer_score += 1
    elif player_choice == "r" and computer_choice == "s":
      print("You win! Rock beats Scissors.")
      player_score += 1
    elif player_choice == "r" and computer_choice == "r":
      print("That's a draw.")
    elif player_choice == "p" and computer_choice == "r":
      print("You win! Paper beats Rock.")
      player_score += 1
    elif player_choice == "p" and computer_choice == "s":
      print("You lost! Scissors beats Paper.")
      computer_score += 1
    elif player_choice == "p" and computer_choice == "p":
      print("That's a draw.")
    elif player_choice == "s" and computer_choice == "r":
      print("You lost! Rock beats Scissors.")
      computer_score += 1
    elif player_choice == "s" and computer_choice == "p":
      print("You win! Scissors beats Paper.")
      player_score += 1
    elif player_choice == "s" and computer_choice == "s":
      print("That's a draw.")
    else:
      print("Invalid input. Please try again.")
    if player_score == 3:
      print("Congrates! you Win!!!")
      break
    elif computer_score == 3:
      print("Sorry, you lost. Better luck next time.")
      break
  print("Final scores:")
  print(f"{user_name}: {player_score}")
  print(f"Computer: {computer_score}")

def main():
  while True:
    play_game()
    play_again = input("Do you want to play again? (Y/N) ").lower()
    if play_again != "y":
      break

if __name__ == "__main__":
  main()
