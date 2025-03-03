import random

def show_message(message='Play the Nim Game 🥢') -> None:
   print(message)

# map the limit of the number of sticks taken from the heap per player to the divisor
def get_divisor(value: int) -> int:
   """
     alternative: return value + 1
   """
   # game variation should be limited to these options for now
   # value => 2, divisor => 3 (i.e. multiples of 3)
   # value => 3, divisor => 4 (i.e. multiples of 4)
   # value => 4, divisor => 5 (i.e. multiples of 5)
   if value == 2: return 3
   if value == 3: return 4
   return 5

"""Computer player
   :param sticks: int - number of sticks in the heap
   :return: int - number of sticks removed by the computer player
"""
def nim(sticks: int, limit: int) -> int:
   # set a range of the maximum allowed number of sticks to remove
   maximum_move = min(limit, sticks)
   move = random.randint(1, maximum_move)
   return move


"""Human player
   :param sticks: int - number of sticks in the heap
   :return: int - number of sticks removed by the human player
"""
def nim_human(sticks: int, limit: int) -> int:
   while True:
      try:
         move = int(input(f'Enter the number of sticks to remove between (1-{limit}) inclusive:\n'))
         if move > sticks:
            raise ValueError('number of sticks removed cannot exceed the total sticks')

         if move < 1 or move > limit:
            raise ValueError(f'Invalid number of sticks! Please enter the sticks to remove within the range (1-{limit})')

         return move
      except ValueError as error:
         show_message(f'error: {error}')


"""Smart computer player
   :param sticks: int - number of sticks in the heap
   :return: int - number of sticks removed by the super player
"""
def nim_best(sticks: int, limit: int) -> int:
   divisor = get_divisor(limit)
   # determine the most optimal move strategy
   remainder = sticks % divisor
   # if the smart computer is in loosing position, play a legal move regardless
   # otherwise play an optimal move
   return nim(sticks, limit) if remainder == 0 else remainder

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

"""Game Variation
   :return: int - maximum number of sticks or less a player can take

   limit = 2, players can take up to 2 sticks max. i.e (1<=sticks<=2)
   as loosing position will be multiples of 3

   limit = 3, standard condition: players can take up to 3 sticks. i.e (1<=sticks<=3)
   as loosing position will be multiples of 4

   limit = 4, players can take up to 4 sticks max. i.e (1<=sticks<=4)
   as loosing position will be multiples of 5

   limit = n, players can take up to 4 sticks max. i.e (1<=sticks<=n)
   as loosing position will be multiples of n+1
"""
def game_variation() -> int:
   while True:
      try:
          limit = int(input(f'Provide the maximum number of sticks players can take from the heap at a time (between 2-4 inclusive):\n'))
          if limit >= 2 and limit <= 4:
             return limit
          show_message('Invalid limit. value must be between 2-4 range inclusive')
      except ValueError:
         show_message('Invalid data type for input')


"""Game Manager
   :return: tuple - player types and no of sticks in the heap
"""
def setup_game():
   show_message()
   player_one = get_player_type(1)
   player_two = get_player_type(2)
   limit = game_variation()

   while True:
      try:
         sticks = int(input('Enter the number of sticks between 10-100 inclusive to add to the heap: \n'))
         if sticks < 10 or sticks > 100:
            raise ValueError('Number of sticks is not within the range. Please try again')

         return sticks, player_one, player_two, limit
      except ValueError as err:
         show_message(f'error: {err}')


"""Game Controller
"""
def play_game(sticks: int, player_one: str, player_two: str, limit: int) -> None:
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
      move = players[current_player](sticks, limit)
      # keep track of sticks
      sticks-=move

      show_message(f'{player_labels[current_player]} player {current_player + 1} removed {move} sticks')
      show_message(f'Total sticks left: {sticks}')

      # no more sticks? current player wins
      if sticks == 0:
         show_message(f'Game over! {player_labels[current_player]} player {current_player + 1} wins 🚀🎉')
         break

      # switch player
      current_player = 1 if current_player == 0 else 0


def main():
    while True:
      sticks, player_one, player_two, limit = setup_game()
      show_message(f'Game state: {(sticks, player_one, player_two, limit)}')
      play_game(sticks, player_one, player_two, limit)

      response = input('Do you want to play again? type (yes or no):\n')

      response = response.strip().lower()

      if response != "yes":
         show_message('See you next time. 👋')
         break

if __name__ == "__main__":
   main()