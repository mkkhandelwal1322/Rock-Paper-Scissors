import random  #  for random to work
import os  #  for clrscr function to work

#  classic game - Rock, Paper, Scissors
#  tuples list of win combinations
WIN_LIST_RPS = [('ROCK', 'SCISSORS'),  # who can be defeated by ROCK
                ('SCISSORS', 'PAPER'),  # who can be defeated by SCISSORS
                ('PAPER', 'ROCK')]  # who can be defeated by PAPER
#  list of selections
SELECTIONS_LIST_RPS = ['ROCK', 'PAPER', 'SCISSORS']

#  an expansion of classic game - Rock, Paper, Scissors, Lizard, Spock
#  tuples list of win combinations
WIN_LIST_RPSLS = [('ROCK', 'SCISSORS'),  # who can be defeated by ROCK
                  ('SCISSORS', 'PAPER'),  # who can be defeated by SCISSORS
                  ('PAPER', 'ROCK')]  # who can be defeated by PAPER

#  list of selections
SELECTIONS_LIST_RPSLS = ['ROCK','PAPER','SCISSORS']

#  dictionary that saves wins of both player and computer, and ties
stats_count = {'player':0, 'computer':0, 'ties':0}

def clrscr():
  """ Clears the console in order to make a more pleasant game """
  if os.name == "posix":  # compatible with Unix/Linux/MacOS/BSD/etc
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"):  # compatible with DOS/Windows
    os.system('CLS')

def welcome():
  """ Main menu for the Game """
  clrscr()
  while True:
    option = input(
      "************** Welcome to my Rock-Paper-Scissors based Games ******************"
    "\n*******************************************************************************"
    "\n*                                OPTIONS                                      *"
    "\n*******************************************************************************"
    "\n* [1] - Rock Paper Scissors                                         *"
    "\n* [2] - Exit                                                                  *"                   
    "\n*******************************************************************************"
    "\n Please select an option (1, or 2): ")
    if option == '1':  #  if options 1 is selected, it will call lets_play function
      lets_play(option)
    elif option == '2':  # if option is 2, exits the program
      print("Bye bye")
      exit()
    else:  #  if there's an invalid option, the menu will start again
      input("Invalid option. Try again... Please press ENTER to continue")
      clrscr()
    
def lets_play(option):
  """ A function that sets which game is going to be played based on the option selected """
  clrscr()
  
  if option == '1':  #  if option 1 is selected, it will play Rock + Paper + Scissors game
    intro = (" Welcome to Rock + Paper + Scissors game!")  
    option_help = ("\n This game is simple and goes as following:"  
          "\n *You can choose between: Rock, Paper or Scissors."
          "\n\n You must take in consideration that:"
          "\n *Rock crushers Scissors."
          "\n *Scissors cut Paper."
          "\n *Paper covers Rock."
          "\n\n Notes: *The first one that scores 5 points WINS the game!"
          "\n        *If you forgot the rules, just type 'help'."
          "\n        *If you want to go to main menu to try the other games, just type 'quit'."
          "\n        *If you want to exit because you're afraid of loosing, just type 'exit' you coward!\n")
    selections_list = SELECTIONS_LIST_RPS  #  selections are assigned based on the game
    win_list = WIN_LIST_RPS  #  win list is assigned based on the game
 
  print(intro)  #  displays the intro information based on the option selected
  print(option_help)  # displays the help information based on the option selected
    
  while True:
    player_selection = input("Your Selection {}: ".format(selections_list))
    player_selection = player_selection.upper()
    
    if player_selection in selections_list:
      clrscr()
      computer_selection = random.choice(selections_list)
      
      print("Player Selection: {}".format(player_selection))
      print("Computer Selection: {}".format(computer_selection))
      
      match = player_selection, computer_selection  #  converts the player's and computer's selection into a tuple to compare it to win list
      
      if player_selection == computer_selection:  #  if both selections (player and computer) are the same, a tie count is added to the dictionary
        stats_count['ties'] += 1
        print("\nResult: Both are {}! So that's a Tie!".format(player_selection))
      elif match in win_list:  #  if the tuple is the same as the win_list, player wins and a player count is added to the dictionary
        stats_count['player'] += 1
        print("\nResult: The power of {} beats {}! You won!".format(player_selection, computer_selection))
      else:  #  if none of the conditions above are true, computer wins and a computer count is added to the dictionary
        stats_count['computer'] += 1
        print("\nResult: The power of {} is stronger than {}! You lost!".format(computer_selection, player_selection))
      print("-------  STATS  -------"
            "\n YOU  | COMPUTER | DRAW"
            "\n  {player}        {computer}        {ties}"
            "\n-----------------------".format(**stats_count))
      if stats_count['player'] == 5:  #  if player gets 5 points, he wins
        print("The game is DONE! You won! Congratulations!")
        exit()
      elif stats_count['computer'] == 5:  #  if computer gets 5 points, he wins
        print("The game is DONE! You lost against a perfectly designed AI! You're now in the wall of shame!")
        exit()
    elif player_selection == 'HELP':  #  if the user doesn't remember the rules, it will show them again
      clrscr()
      print(option_help)
    elif player_selection == 'QUIT':  #  if the user wants to play another game, it will take him to main menu, stats are again
      stats_count['player'] = 0
      stats_count['computer'] = 0
      stats_count['ties'] = 0
      input("Let's try another game mode then. I hope you enjoyed! Please press ENTER to continue...")
      clrscr()
      break
    elif player_selection == 'EXIT':  #  if the user wants to exit the game
      print("Bye bye... YOU COWARD!")
      exit()
    else:
      print("Invalid selection. Try again...")  #  if there's an invalid choice, the input will show again

#  beginning of program        
welcome()
