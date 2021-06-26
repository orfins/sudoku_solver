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
