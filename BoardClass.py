class Board:
    def __init__(self, size: int = 3):
        self._tiles = self._generate_blank_rows(size)
        self._size = size
        self._moves = 0

    def get_board(self):
        return self._tiles

    def print_board(self, show_cordinates=True):
        # Underline and underline_end character modifier sequences
        ul = "\033[4m"
        ule = "\033[0m"

        # Print first row with cordinates
        if show_cordinates:
            first_number = True
            last_number = False
            print(ul + " |" + ule, end='')
            for column in range(self._size):
                separator = '|' if not last_number else ' '
                if first_number:
                    separator = ''
                    first_number = False
                print(ul + "{}{}".format(separator, column) + ule, end='')
                if column == (self._size - 1):
                    print(ul + " " + ule, end='')
            print()

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
                        print("{}│".format(row), end='')
                print(ul + "{}{}".format(separator, char) + ule, end='')
                if column == (self._size - 1):
                    print("│", end='')
            print()

    def set_tile(self, row: int, column: int, char: str):
        if self._tiles[row][column] is not None:
            raise OccupiedSpaceError
        else:
            self._tiles[row][column] = char
            self._moves += 1
            # TODO check for win here & end game

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

    @staticmethod
    def _generate_blank_rows(size: int):
        tiles = []
        blank_row = [None for i in range(int(size))]
        for i in range(int(size)):
            tiles.append(blank_row[:])

        return tiles


class OccupiedSpaceError(Exception):
    pass
