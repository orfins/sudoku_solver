from itertools import chain

from sudoku_solver.structures import Board, Cell


def attempt_certain_fill(cell: Cell) -> bool:
    """
    Find a certain fill for the cell if any.
    :return: Found and filled or failed.
    """
    if len(cell.possible_values) == 0:
        return False
    elif len(cell.possible_values) == 1:
        cell.value = cell.possible_values[0]

        return True
    else:
        for value in cell.possible_values:
            for area in ['square', 'row', 'col']:
                can_other_cell_in_area_be_assigned_the_value = any(c for c in cell.__getattribute__(area) if
                                                                   c is not cell and c.can_fill(value))

                if not can_other_cell_in_area_be_assigned_the_value:
                    cell.value = value

                    return True

    return False


def certain_fills(board: Board):
    """
    Find and fill all certain fills in the board.
    """
    # List comprehension because any() returns on first False and I don't want to re-iterate over the first cells.
    # It is a lot faster this way.
    while any([attempt_certain_fill(cell) for cell in board.cells]):
        pass


def guess_fills(board: Board):
    # while board.is_solvable() and not board.is_complete():
    while board.is_solvable() and not board.is_complete():
        certain_fills(board)

        # When no certain fill found we can start guessing.
        if not board.is_complete():
            # Look for 2 cells in the same row / col / square with same possible_values
            for cell in board.cells:
                if len(cell.possible_values) == 2:
                    for other_cell in chain(cell.row, cell.col, cell.square):
                        if cell is not other_cell and cell.possible_values == other_cell.possible_values:
                            digit_1, digit_2 = cell.possible_values

                            board_copy = board.copy()

                            board_copy.at(*cell.indexes).value = digit_1
                            board_copy.at(*other_cell.indexes).value = digit_2

                            if guess_fills(board_copy):
                                for c in board_copy.cells:
                                    board.at(*c.indexes).value = c.value

                                return True
                            else:
                                cell.value = digit_2
                                other_cell.value = digit_1
                            break

    return board.is_complete()
