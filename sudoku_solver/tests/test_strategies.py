from sudoku_solver.structures import Board
from sudoku_solver.strategies import attempt_certain_fill, certain_fills
from .boards import board_values_by_difficulty


def test_attempt_certain_fill():
    board = Board(board_values_by_difficulty['easy1'])

    print(board.at(0, 0).possible_values)

    assert not attempt_certain_fill(board.at(0, 1))
    assert board.at(0, 1) == 1

    assert attempt_certain_fill(board.at(0, 0))
    assert board.at(0, 0) == 5

    assert board.at(4, 3).possible_values == [1, 3]
    assert attempt_certain_fill(board.at(4, 3))
    assert board.at(4, 3) == 1


def test_certain_fills():
    board = Board(board_values_by_difficulty['easy1'])
    certain_fills(board)
    solution = ((5, 1, 7, 4, 9, 6, 8, 3, 2),
                (9, 3, 6, 2, 1, 8, 7, 4, 5),
                (8, 2, 4, 7, 5, 3, 1, 9, 6),
                (1, 4, 5, 9, 6, 2, 3, 7, 8),
                (6, 7, 3, 1, 8, 5, 4, 2, 9),
                (2, 9, 8, 3, 7, 4, 5, 6, 1),
                (7, 6, 2, 5, 3, 1, 9, 8, 4),
                (4, 5, 9, 8, 2, 7, 6, 1, 3),
                (3, 8, 1, 6, 4, 9, 2, 5, 7))

    assert board.rows == solution

    board = Board(board_values_by_difficulty['medium1'])
    certain_fills(board)
    solution = ((6, 4, 8, 9, 7, 5, 2, 3, 1),
                (9, 3, 2, 6, 4, 1, 7, 5, 8),
                (7, 5, 1, 2, 8, 3, 4, 9, 6),
                (4, 2, 6, 7, 3, 8, 9, 1, 5),
                (5, 8, 9, 1, 2, 6, 3, 4, 7),
                (1, 7, 3, 5, 9, 4, 6, 8, 2),
                (2, 9, 5, 4, 1, 7, 8, 6, 3),
                (8, 6, 4, 3, 5, 2, 1, 7, 9),
                (3, 1, 7, 8, 6, 9, 5, 2, 4))

    assert board.rows == solution

    board = Board(board_values_by_difficulty['medium2'])
    certain_fills(board)
    solution = ((8, 3, 2, 5, 1, 7, 4, 9, 6),
                (7, 4, 5, 9, 3, 6, 2, 1, 8),
                (1, 9, 6, 8, 2, 4, 7, 5, 3),
                (5, 6, 1, 2, 9, 8, 3, 7, 4),
                (3, 7, 8, 1, 4, 5, 9, 6, 2),
                (4, 2, 9, 6, 7, 3, 1, 8, 5),
                (9, 8, 4, 7, 6, 2, 5, 3, 1),
                (6, 1, 3, 4, 5, 9, 8, 2, 7),
                (2, 5, 7, 3, 8, 1, 6, 4, 9))

    assert board.rows == solution

    board = Board(board_values_by_difficulty['hard2'])
    certain_fills(board)
    solution = ((4, 2, 7, 9, 1, 3, 5, 8, 6),
                (9, 1, 5, 6, 8, 7, 3, 2, 4),
                (6, 8, 3, 2, 5, 4, 1, 7, 9),
                (1, 3, 2, 4, 7, 9, 6, 5, 8),
                (7, 6, 4, 5, 3, 8, 2, 9, 1),
                (5, 9, 8, 1, 6, 2, 7, 4, 3),
                (8, 7, 1, 3, 4, 5, 9, 6, 2),
                (3, 4, 9, 7, 2, 6, 8, 1, 5),
                (2, 5, 6, 8, 9, 1, 4, 3, 7))

    assert board.rows == solution

    board = Board(board_values_by_difficulty['hard3'])
    certain_fills(board)
    solution = ((6, 5, 8, 1, 3, 2, 4, 9, 7),
                (7, 4, 3, 5, 9, 8, 1, 2, 6),
                (2, 9, 1, 7, 6, 4, 5, 8, 3),
                (5, 8, 6, 4, 2, 7, 9, 3, 1),
                (3, 2, 4, 9, 1, 5, 6, 7, 8),
                (1, 7, 9, 6, 8, 3, 2, 4, 5),
                (4, 3, 7, 2, 5, 6, 8, 1, 9),
                (8, 1, 5, 3, 4, 9, 7, 6, 2),
                (9, 6, 2, 8, 7, 1, 3, 5, 4))

    assert board.rows == solution

    board = Board(board_values_by_difficulty['hard1'])
    certain_fills(board)
    assert not board.is_complete()

    board = Board(board_values_by_difficulty['expert1'])
    certain_fills(board)
    assert not board.is_complete()
