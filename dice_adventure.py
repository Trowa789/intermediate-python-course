import random
import sys

def main():
  # Player Name
  player_name = str(input('What is your name adventurer? '))
  print(f'Welcome to the game {player_name}! Here you will battle it out in 3 battles using your best dice')
  print('Let the battle commence!!')
  for number in range(1,4):
    def round(number):
      win_con = 3 if number < 3 else 6
      print(f'Welcome to Round {number}! To get through this round, you need to roll a {win_con} or higher')
      decision = input('Are you ready? Y/N \n').lower()
      if decision == 'y':
        dice = random.randint(1,6)
        print(f'You rolled a {dice}!')
        if dice >= win_con:
          if number == 3:
            print('Congrats!! You are a winner!!')
          else:
            print(f'You have won this round!! You may proceed to Round {number+1}!!')
            return True
        else:
          print('You lose!! Better luck next time.')
          sys.exit() # Ends program after losing
      if decision == 'n':
        print('See you next time!!')
        sys.exit() # Ends program if user no longer wishes to continue
    round(number)

if __name__== "__main__":
    main()



