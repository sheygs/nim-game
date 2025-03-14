from utils import show_message, get_player_type, game_rules_variant, nim, nim_human, nim_best

"""Game Manager
   :return: tuple - player types, total no of sticks and sticks limit
"""
def setup_game():
   show_message()
   player_one = get_player_type(1)
   player_two = get_player_type(2)
   limit = game_rules_variant()

   while True:
      try:
         sticks = int(input('Enter the total number of sticks between 10 and 100 inclusive: \n'))
         if sticks < 10 or sticks > 100:
            raise ValueError('number of sticks is not within the range. Please try again')

         return sticks, player_one, player_two, limit
      except ValueError as error:
         show_message(f'error: {error}')


"""Game Controller
"""
def play_game(*args) -> None:
   sticks, player_one, player_two, limit = args

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
      show_message(f'total sticks left: {sticks}')

      # no more sticks? current player wins
      if sticks == 0:
         show_message(f'Game over! {player_labels[current_player]} player {current_player + 1} wins 🚀🎉')
         break

      # switch player
      current_player = 1 if current_player == 0 else 0
      # current_player = (current_player + 1) % 2


def main():
    while True:
      sticks, player_one, player_two, limit = setup_game()
      show_message(f'game state: {(sticks, player_one, player_two, limit)}')
      play_game(sticks, player_one, player_two, limit)

      response = input('Do you want to play again? type (yes or no):\n')

      response = response.strip().lower()

      if response not in ["y", "yes"]:
         show_message('See you next time. 👋')
         break

if __name__ == "__main__":
   main()