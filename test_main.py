import unittest
from check_win import check_win

class TestCheckWin(unittest.TestCase):
    def test_rows(self):
        arr = [['x', 'x', 'x'], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(check_win(arr, 'x'), 'x')

        arr = [[0, 0, 0], ['o', 'o', 'o'], [0, 0, 0]]
        self.assertEqual(check_win(arr, 'o'), 'o')

        arr = [[0, 0, 0], [0, 0, 0], ['x', 'x', 'x']]
        self.assertEqual(check_win(arr, 'x'), 'x')

    def test_columns(self):
        arr = [['x', 0, 0], ['x', 0, 0], ['x', 0, 0]]
        self.assertEqual(check_win(arr, 'x'), 'x')

        arr = [[0, 'o', 0], [0, 'o', 0], [0, 'o', 0]]
        self.assertEqual(check_win(arr, 'o'), 'o')

        arr = [[0, 0, 'x'], [0, 0, 'x'], [0, 0, 'x']]
        self.assertEqual(check_win(arr, 'x'), 'x')

    def test_diagonals(self):
        arr = [['x', 0, 0], [0, 'x', 0], [0, 0, 'x']]
        self.assertEqual(check_win(arr, 'x'), 'x')

        arr = [[0, 0, 'o'], [0, 'o', 0], ['o', 0, 0]]
        self.assertEqual(check_win(arr, 'o'), 'o')

    def test_draw(self):
        arr = [['x', 'o', 'x'], ['o', 'x', 'x'], ['o', 'x', 'o']]
        self.assertTrue(check_win(arr, 'x'))
        self.assertTrue(check_win(arr, 'o'))
