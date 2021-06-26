from sudoku_solver.structures import Board
from sudoku_solver.strategies import attempt_certain_fill, certain_fills, guess_fills
from .boards import board_values_by_difficulty


def test_attempt_certain_fill():
    board = Board(board_values_by_difficulty['easy1']['problem'])

    print(board.at(0, 0).possible_values)

    assert not attempt_certain_fill(board.at(0, 1))
    assert board.at(0, 1) == 1

    assert attempt_certain_fill(board.at(0, 0))
    assert board.at(0, 0) == 5

    assert board.at(4, 3).possible_values == [1, 3]
    assert attempt_certain_fill(board.at(4, 3))
    assert board.at(4, 3) == 1


def test_certain_fills():
    # Solvable with certain fills
    for difficulty in ['easy1', 'medium1', 'medium2', 'hard2', 'hard3']:
        board = Board(board_values_by_difficulty[difficulty]['problem'])
        certain_fills(board)
        assert board.rows == board_values_by_difficulty[difficulty]['solution'], difficulty

    # Not solvable with certain fills
    for difficulty in ['hard1', 'expert1']:
        board = Board(board_values_by_difficulty[difficulty]['problem'])
        certain_fills(board)
        assert not board.is_complete()


def test_guess_fills():
    for difficulty in ['hard1', 'expert1']:
        board = Board(board_values_by_difficulty[difficulty]['problem'])
        guess_fills(board)

        assert board.rows == board_values_by_difficulty[difficulty]['solution'], difficulty
