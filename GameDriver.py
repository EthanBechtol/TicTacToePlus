from BoardClass import Board, OccupiedSpaceError, InvalidInputError, BoardFullError
from TimerManager import TimerManager


def init_players():
    valid_player_num = False
    while not valid_player_num:
        num_players = int(input("Enter the desired number of players:\n"))
        if num_players >= 2:
            valid_player_num = True
        else:
            print("The number of players must be 2 or above!")
    players = []
    for index, player in enumerate(range(num_players)):
        valid_char = False
        desired_char = ''
        while not valid_char:
            desired_char = input(f"Player {index}, what character would you like to be? (i.e. 'x', 'o', etc.)\n")
            if len(desired_char) == 1:
                players.append(desired_char)
                valid_char = True
            else:
                print("Invalid selection. Please enter a single letter to be your character.")
    return players


def process_turn(game: Board, players: list, player_turn: int, timers: TimerManager):
    valid_move = False
    while not valid_move:
        if game.check_capacity() == 0:
            raise BoardFullError

        print("Current board:")
        game.print_board()

        timers.start_timer(players[player_turn])
        try:
            move = input(f"Player {players[player_turn]}, make your move:\n")
            move = move.split()
            if len(move) != 2:
                raise InvalidInputError
            game.set_tile(int(move[0]), int(move[1]), players[player_turn])
            valid_move = True
        except OccupiedSpaceError:
            print("Invalid move. That space is already occupied). Try again.")

        except InvalidInputError:
            print("Invalid input. Please enter two coordinates (row & column) separated by a space.")

        else:
            timers.end_timer(players[player_turn])
            player_turn = player_turn + 1 if player_turn + 1 != len(players) else 0
            return player_turn


def init_board(board: Board):
    valid_board_size = False
    board_size = 3
    while not valid_board_size:
        board_size = int(input("How big would you like the board to be? (Enter an integer)\n"))
        if board_size >= 3:
            valid_board_size = True
            board.reset(board_size)
        else:
            print("The board size must be 3 or greater.")
    return board


def main():
    running = True
    game = Board()
    player_turn = 0
    player_timers = TimerManager()

    while running:
        in_game = True

        # Initialize player list & board
        players = init_players()
        init_board(game)

        while in_game:
            try:
                # Processes the turn AND advances who's turn it is.
                player_turn = process_turn(game, players, player_turn, player_timers)
            except BoardFullError:
                print("All spaces have become occupied!")
                in_game = False

            else:
                if game.winner is not None:
                    in_game = False

        game.print_endscreen(player_timers)

        play_again = input("Would you like to start a new game? (Enter 'yes' or 'y' if so)\n")
        if play_again.lower() not in ("yes", 'y'):
            running = False
            print("Terminating program. Thank you for playing!")


if __name__ == '__main__':
    main()
