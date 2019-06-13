def manhattan_dist(tile, other):
        (i, j), (k, l) = tile, other
        return abs(i - k) + abs(j - l)

class GameBoard():
    @staticmethod
    def solved_board(n):
        b = [[i*n+j+1 for j in range(n)] for i in range(n)]
        b[n-1][n-1] = None
        return b

    def valid_pos(self, tile):
        i, j = tile
        return (0 <= i < self.dimension and
           0 <= j < self.dimension)

    def get(self, i, j):
        return self.grid[j][i] if self.valid_pos((i, j)) else None

    def can_swap(self, tile):
        return (self.valid_pos(tile) and
            manhattan_dist(tile, self.hole) == 1)

    def swap(self, tile):
        if self.can_swap(tile):
            (i, j), (k, l) = tile, self.hole
            self.grid[j][i], self.grid[l][k] = (
                self.grid[l][k], self.grid[j][i])
            self.hole = (i, j)

    def neighbors(self, tile):
        return [(i, j) for (i, j), _ in self.enumerate_tiles() if manhattan_dist(tile, (i,j)) == 1]

    # TODO: Try not to swap with previous swapped tile
    def shuffle(self, times):
        from random import choice
        for _ in range(times):
            hole_neighbors = self.neighbors(self.hole)
            self.swap(choice(hole_neighbors))

    def win_state(self):
        # Hole should be last tile
        if self.hole != (self.dimension - 1, self.dimension - 1):
            return False

        tiles = list(self.tiles())
        t_prev = -1
        # Every tile should be ordered
        for t in tiles[:len(tiles)-1]:
            if t_prev >= t:
                return False

            t_prev = t

        return True

    def enumerate_tiles(self):
        for j in range(self.dimension):
            for i in range(self.dimension):
                yield ((i, j), self.get(i, j))

    def tiles(self):
        for (_, _), n in self.enumerate_tiles():
            yield n

    def __init__(self, n):
        self.dimension = n
        self.grid = GameBoard.solved_board(n) if n >= 1 else []
        self.hole = (n-1, n-1)

    def __str__(self):
        s = ''
        for r in self.grid:
            s += ' '.join([str(i) if i is not None else ' ' for i in r]) + '\n'

        return s