import random

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
         print(f'error: {error}')


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
      choice = int(input(f'Select a game type for player {player_num}:\n1. Computer\n2. Human\n3. Smart Computer.\nType a number between 1-3 inclusive\n'))
      match choice:
         case 1:
            return "computer"
         case 2:
            return "human"
         case 3:
            return "smart"
         case _:
            raise ValueError('Invalid user choice. Please try again')
   # catch non-integer inputs
   except ValueError as error:
      # recursively ask the player for choice until valid
      print(f'error: {error}')
      return get_player_type(player_num)


# print(f'human player removed: {nim_human(11)}')
# print(f'computer player removed: {nim(11)}')
# print("smart player removed: ", nim_best(11))
print(f'player type: {get_player_type(1)}')