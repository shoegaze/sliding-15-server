import unittest
from numgame import GameBoard

class TestGameBoard(unittest.TestCase):
    def test_solved_board(self):
        n = 3
        b = GameBoard(n)

        nprev = -1
        for t in b.tiles():
            if t is not None:
                self.assertGreater(t, nprev, "Each element should be ordered.")
            nprev = t

        total = sum([t for t in b.tiles() if t])
        self.assertEqual(total, 36, "Sum of all elements should be 36.")
        holes = sum([1 for t in b.tiles() if t is None])
        self.assertEqual(holes, 1, "There should only be one hole.")

    def test_valid_pos(self):
        n = 3
        b = GameBoard(n)

        self.assertTrue(b.valid_pos((2, 2)), "Should return true for position within grid.")
        self.assertFalse(b.valid_pos((-1, 0)) or b.valid_pos((0, 3)), "Should return false on OOB.")

    def test_get(self):
        n = 3
        b = GameBoard(n)

        self.assertEqual(b.get(2, 0), 3, "Should return tile value for in bound indices.")
        self.assertTrue(b.get(-1, 0) is None and b.get(0, 3) is None, "Should return None on OOB.")

    def test_swap(self):
        n = 3
        b = GameBoard(n)
        target = (2,1)

        self.assertEqual(b.get(*target), 6, "Value before swap should be unchanged.")
        b.swap(target)
        self.assertIsNone(b.get(*target), "Value after swap should be changed.")
        self.assertEqual(b.hole, target, "The new tile should be the hole.")

    def test_neighbors(self):
        n = 3
        b = GameBoard(n)

        corner = (0,0)
        self.assertListEqual(b.neighbors(corner), [(1, 0), (0, 1)], "Corner tiles should have 2 neighbors.")
        middle = (1,1)
        self.assertListEqual(b.neighbors(middle), [(1, 0), (0, 1), (2, 1), (1, 2)], "Middle tiles should have 4 neighbors.")
        side = (2,1)
        self.assertListEqual(b.neighbors(side), [(2, 0), (1, 1), (2, 2)], "Side tiles should have 3 neighbors.")

    def test_shuffle(self):
        pass
        # n = 3
        # b = GameBoard(n)

        # TODO

    def test_win_state(self):
        n = 3
        b = GameBoard(n)

        self.assertTrue(b.win_state(), "Default board is already solved.")
        b.swap((2,1))
        self.assertFalse(b.win_state(), "Swapped board is not solved.")


if __name__ == "__main__":
    unittest.main()