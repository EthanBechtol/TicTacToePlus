class Board:
    def __init__(self, size: int = 3):
        self._tiles = []
        self._size = size

        blank_row = [None for i in range(size)]
        for i in range(size):
            self._tiles.append(blank_row[:])

    def get_board(self):
        return self._tiles
