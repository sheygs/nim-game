import random

def show_message(message='Play the Nim Game 🥢'):
   print(message)

"""Computer player
   :param sticks: int - number of sticks in the heap
   :return: int - number of sticks removed by the computer player
"""
def nim(sticks: int) -> int:
   # set a range of the maximum allowed number of sticks to remove
   maximum_move = min(3, sticks)
   move = random.randint(1, maximum_move)
   return move


"""Human player
   :param sticks: int - number of sticks in the heap
   :return: int - number of sticks removed by the human player
"""
def nim_human(sticks: int) -> int:
   while True:
      try:
         move = int(input('Enter the number of sticks to remove between (1-3) inclusive: \n'))
         if move > sticks:
            raise ValueError('number of sticks removed cannot exceed the total sticks in the heap')

         if move < 1 or move > 3:
            raise ValueError('Invalid number of sticks! Please enter the sticks to remove within the range (1-3)')

         return move
      except ValueError as error:
         show_message(f'error: {error}')


"""Super/Smart computer player
   :param sticks: int - number of sticks in the heap
   :return: int - number of sticks removed by the super player
"""
def nim_best(sticks: int) -> int:
   # determine the most optimal move strategy
   remainder = sticks % 4
   # if the smart computer is in loosing position, play a legal move regardless
   # otherwise play an optimal move
   return nim(sticks) if remainder == 0 else remainder

"""Player type
   :param player_num: int - player rank/position
   :return: str - player mode
"""
def get_player_type(player_num:int) -> str:
   try:
      choice = int(input(f'Select a game type for player {player_num}:\n1. Human\n2. Computer\n3. Smart Computer.\nType a number between 1-3 inclusive\n'))
      match choice:
         case 1:
            return "human"
         case 2:
            return "computer"
         case 3:
            return "smart"
         case _:
            raise ValueError('Invalid user choice. Please try again')
   # catch non-integer inputs
   except ValueError as error:
      # recursively ask the player for choice until valid
      show_message(f'error: {error}')
      return get_player_type(player_num)


"""Game Manager
   :return: tuple - player types and no of sticks in the heap
"""
def setup_game():
   show_message()
   player_one = get_player_type(1)
   player_two = get_player_type(2)

   while True:
      try:
         sticks = int(input('Enter the number of sticks between 10-100 inclusive to add to the heap: \n'))
         if sticks < 10 or sticks > 100:
            raise ValueError('Number of sticks is not within the range. Please try again')

         return sticks, player_one, player_two
      except ValueError as err:
         show_message(f'error: {err}')


"""Game Controller
"""
def play_game(sticks: int, player_one: str, player_two: str):
   show_message(f'Total sticks in the heap: {sticks}')

   move_mapper = {
      "human": nim_human,
      "computer": nim,
      "smart": nim_best
   }

   player_choices = {
      "human": "Human",
      "computer": "Computer",
      "smart": "Smart"
   }

   players = [
         move_mapper[player_one],
         move_mapper[player_two]
   ]

   player_labels = [
        player_choices[player_one],
        player_choices[player_two]
   ]

   # current player index
   current_player = 0

   while sticks > 0:
      # current player make moves
      move = players[current_player](sticks)
      show_message(f'{player_labels[current_player]} player {current_player + 1} removed {move} sticks')

      # keep track of sticks
      sticks-=move
      show_message(f'Total sticks left: {sticks}')

      # no more sticks? current player wins
      if sticks == 0:
         show_message(f'Game over! {player_labels[current_player]} player {current_player + 1} wins 🚀🎉')
         break

      # switch player
      current_player = 1 if current_player == 0 else 0
      # current_player = (current_player + 1) % 2

def main():
    sticks, player_one, player_two = setup_game()
    show_message(f'Game state: {(sticks, player_one, player_two)}')
    play_game(sticks, player_one, player_two)

if __name__ == "__main__":
   main()