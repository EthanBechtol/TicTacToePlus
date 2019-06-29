class Board:
    def __init__(self, size: int = 3):
        self._tiles = []
        self._size = size

        blank_row = [None for i in range(size)]
        for i in range(size):
            self._tiles.append(blank_row[:])

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
