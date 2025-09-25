import random

def show_message(message='Play the Nim Game 🥢') -> None:
    print(message)

# the divisor is the maximum number of sticks (limit) taken from the heap plus one
"""
   :param limit: int - maximum number of sticks that can be removed
   :return: int - limit + 1
"""
def get_divisor(limit: int) -> int:
    # game variation limited to these options for now
    # loosing positions
    # limit => 2, divisor => 3 (i.e. multiples of 3)
    # limit => 3, divisor => 4 (i.e. multiples of 4)
    # limit => 4, divisor => 5 (i.e. multiples of 5)
    if limit == 2: return 3
    if limit == 3: return 4
    return 5

"""Computer player
   :param sticks: int - number of sticks in the heap
   :param limit: int - maximum number of sticks that can be removed
   :return: int - number of sticks removed by the computer player
"""
def nim(sticks: int, limit: int) -> int:
    # set a range of the maximum allowed number of sticks to remove
    max_move = min(limit, sticks)
    move = random.randint(1, max_move)
    return move


"""Human player
   :param sticks: int - number of sticks in the heap
   :param limit: int - maximum number of sticks that can be removed
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
   :param limit: int - maximum number of sticks that can be removed
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
def get_player_type(player_num: int) -> str:
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
         # recursively run until valid choice is provided
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

   limit = n, players can take up to `n` sticks max. i.e (1<=sticks<=n)
   as loosing position will be multiples of n+1
"""
def game_rules_variant() -> int:
    while True:
       try:
           limit = int(input(f'Enter the maximum number of sticks players can take from the heap at a time (between 2-4 inclusive):\n'))
           if limit >= 2 and limit <= 4:
              return limit
           show_message('limit must be between 2-4 inclusive')
       except ValueError:
           show_message('Invalid data type for "limit"')

