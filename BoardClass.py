from TimerManager import TimerManager


class Board:
    def __init__(self, size: int = 3):
        self._tiles = self._generate_blank_rows(size)
        self._size = size
        self._moves = 0
        self.winner = None

    def get_board(self):
        return self._tiles

    @staticmethod
    def _generate_blank_rows(size: int):
        tiles = []
        blank_row = [None for i in range(int(size))]
        for i in range(int(size)):
            tiles.append(blank_row[:])

        return tiles

    def _print_vertical_coords(self):
        offset = len(str(self._size))
        coords = ["{number:$>{width}}".format(number=num, width=offset) for num in range(self._size)]

        for index in range(offset):
            first_number = True
            last_number = False
            ul = "\033[4m" if index == offset - 1 else ''
            ule = "\033[0m" if index == offset - 1 else ''

            print(ul + "{space:{offset}}│".format(space=' ', offset=offset) + ule, end='')
            for coord in coords:

                separator = '│' if not last_number else ' '
                target_num = coord[index] if coord[index] != '$' else ' '
                if first_number:
                    separator = ''
                    first_number = False
                print(ul + "{}{}".format(separator, target_num) + ule, end='')
                if coord == (self._size - 1):
                    print(ul + " " + ule, end='')
            print()

    def print_board(self, show_cordinates=True):
        # Underline and underline_end character modifier sequences
        ul = "\033[4m"
        ule = "\033[0m"
        offset = len(str(self._size))

        # Print first row with cordinates
        if show_cordinates:
            self._print_vertical_coords()

        # Print each individual row
        for row in range(self._size):
            start = True
            for column in range(self._size):
                char = " " if (self._tiles[row][column] is None) else (self._tiles[row][column])
                separator = '│' if not start else ''
                if start:
                    start = False
                    # Add row number if show_cordinates enabled
                    if show_cordinates:
                        print("{row: >{offset}}│".format(row=row, offset=offset), end='')
                print(ul + "{}{}".format(separator, char) + ule, end='')
                if column == (self._size - 1):
                    print("│", end='')
            print()

    def set_tile(self, row: int, column: int, char: str, check_win=True):
        if self._tiles[row][column] is not None:
            raise OccupiedSpaceError
        else:
            self._tiles[row][column] = char
            self._moves += 1

            if self.check_any_win(row, column):
                self.winner = char

    def check_capacity(self, verify=False):
        # Verify parameter inspects each individual space to make sure nothing was changed illegally.
        if not verify:
            return (self._size ** 2) - self._moves
        else:
            free_spaces = 0
            for row in self._tiles:
                for column in row:
                    if column is None:
                        free_spaces += 1

            return free_spaces

    def reset(self, size: int or str = 'same'):
        if size == "same":
            self._tiles = self._generate_blank_rows(self._size)
        elif isinstance(size, int):
            self._tiles = self._generate_blank_rows(size)
        else:
            raise ValueError("Invalid argument: {}. Leave argument blank to keep current size or enter a new size int.")

    def print_endscreen(self, timer_data: TimerManager):
        timers = timer_data.get_timers()

        print()
        print(" --- GAME OVER! ---")
        self.print_board()
        winner = self.winner if self.winner is not None else "Nobody"
        print(f"{winner} won the game!\n"
              "Statistics:\n"
              f"\tMoves made: {self._moves}")
        print("\tHow long players spent making moves:")
        for player, time in timers.items():
            print(f"\t\t{player}: {time:.3f} seconds")

    # Win condition check methods
    def check_any_win(self, row: int, column: int):
        win_status = any([self.check_win_horizontal(row, column),
                          self.check_win_vertical(row, column),
                          self.check_win_slant_left(row, column),
                          self.check_win_slant_right(row, column)])
        return win_status

    def check_win_horizontal(self, row: int, column: int):
        win_char = self._tiles[row][column]
        if win_char is not None:
            if all([x == win_char for x in self._tiles[row]]):
                return True
        return False

    def check_win_vertical(self, row: int, column: int):
        win_char = self._tiles[row][column]
        if win_char is not None:
            for row in self._tiles:
                if row[column] != win_char:
                    return False
            return True
        return False

    def check_win_slant_left(self, row: int, column: int):
        win_char = self._tiles[row][column]
        if (win_char is not None) and (row == column):
            for index, row_array in enumerate(self._tiles):
                if row_array[index] != win_char:
                    return False
            return True
        return False

    def check_win_slant_right(self, row: int, column: int):
        win_char = self._tiles[row][column]
        if win_char is not None:
            current_column = self._size - 1
            for row in self._tiles:
                if row[current_column] != win_char:
                    return False
                current_column -= 1
            return True
        return False


class OccupiedSpaceError(Exception):
    pass


class InvalidInputError(Exception):
    pass

class BoardFullError(Exception):
    pass