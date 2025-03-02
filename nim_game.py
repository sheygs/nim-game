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
            print('number of sticks removed cannot exceed the total sticks in the heap')
            continue

         if move < 1 or move > 3:
            print('Invalid number of sticks! Please enter the sticks to remove within the range (1-3)')
            continue

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
   # if remainder == 0:
   #    move = nim(sticks)
   # otherwise play an optimal move
   # else:
   #    move = remainder
   # return move
   return nim(sticks) if remainder == 0 else remainder

print(f'human player removed: {nim_human(11)}')
print(f'computer player removed: {nim(11)}')
print("smart player removed: ", nim_best(11))