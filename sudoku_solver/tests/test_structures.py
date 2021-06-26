from sudoku_solver.structures import Board, e
from .boards import board_values_by_difficulty


def test_boards_properties_are_built_correctly():
    for values in board_values_by_difficulty.values():
        board = Board(values)
        for row_i in range(len(values)):
            for col_i in range(len(values)):
                assert board.rows[row_i][col_i] == values[row_i][col_i]
                assert board.cols[col_i][row_i] == values[row_i][col_i]
                assert board.at(row_i, col_i).value == values[row_i][col_i].value


def test_cells_retrieve_correct_rows():
    for values in board_values_by_difficulty.values():
        board = Board(values)

        for row in board.rows:
            for cell in row:
                assert row == cell.row


def test_cells_retrieve_correct_cols():
    for values in board_values_by_difficulty.values():
        board = Board(values)

        for col in board.cols:
            for cell in col:
                assert col == cell.col


def test_cells_retrieve_correct_square():
    board = Board(board_values_by_difficulty['easy1'])

    square = board.at(3, 5).square
    assert len(square) == 9
    assert board.at(3, 3) in square
    assert board.at(3, 4) in square
    assert board.at(3, 5) in square
    assert board.at(4, 3) in square
    assert board.at(4, 4) in square
    assert board.at(4, 5) in square
    assert board.at(5, 3) in square
    assert board.at(5, 4) in square
    assert board.at(5, 5) in square

    assert board.at(3, 3).square == square
    assert board.at(3, 4).square == square
    assert board.at(3, 5).square == square
    assert board.at(4, 3).square == square
    assert board.at(4, 4).square == square
    assert board.at(4, 5).square == square
    assert board.at(5, 3).square == square
    assert board.at(5, 4).square == square
    assert board.at(5, 5).square == square


def test_cells_indexes_match_their_location():
    for values in board_values_by_difficulty.values():
        board = Board(values)

        for cell in board.cells:
            assert board.at(*cell.indexes).value == cell.value


def test_cells_is_empty():
    for values in board_values_by_difficulty.values():
        board = Board(values)

        for cell in board.cells:
            assert (cell.value == e) == cell.is_empty()


def test_cells_can_fill():
    for values in board_values_by_difficulty.values():
        board = Board(values)

        for cell in board.cells:
            for digit in board.digits:
                if cell.is_empty():
                    assert cell.can_fill(digit) == (
                            digit not in cell.row and
                            digit not in cell.col and
                            digit not in cell.square)
                else:
                    assert not cell.can_fill(digit)


def test_cells_update_possible_values():
    board = Board(board_values_by_difficulty['easy1'])

    board.at(0, 1).update_possible_values()
    assert board.at(0, 1).possible_values == []

    board.at(0, 0).update_possible_values()
    assert board.at(0, 0).possible_values == [5]

    board.at(0, 2).update_possible_values()
    assert board.at(0, 2).possible_values == [7]

    board.at(1, 2).update_possible_values()
    assert board.at(1, 2).possible_values == [6, 7]

    board.at(6, 2).update_possible_values()
    assert board.at(6, 2).possible_values == [2, 6, 9]


def test_boards_update_possible_values():
    board = Board(board_values_by_difficulty['easy1'])

    assert board.at(0, 1).possible_values == []
    assert board.at(0, 0).possible_values == [5]
    assert board.at(6, 2).possible_values == [2, 6, 9]


def test_cells_update_possible_values_when_assigned():
    board = Board(board_values_by_difficulty['expert1'])

    assert board.at(0, 0).possible_values == [3, 6, 8]
    assert board.at(0, 8).possible_values == [1, 3]

    board.at(0, 0).value = 3

    assert board.at(0, 0).possible_values == []
    assert board.at(0, 8).possible_values == [1]


def test_board_copy_is_deep():
    for values in board_values_by_difficulty.values():
        board = Board(values)
        copied = board.copy()

        assert board is not copied
        for row_i in range(len(values)):
            for col_i in range(len(values)):
                assert board.at(row_i, col_i).value == copied.at(row_i, col_i).value
                assert board.at(row_i, col_i) is not copied.at(row_i, col_i)
