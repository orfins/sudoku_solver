from __future__ import annotations
from itertools import chain
from math import sqrt
from typing import Union, Tuple, cast

e = '_'


class Cell:
    def __init__(self, board, row_i, col_i, value):
        self.__board = board
        self.__row_i = row_i
        self.__col_i = col_i
        self.__value = value

        self.possible_values = []  # For the algorithms to play with.

        self.__square = None

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, v: Union[int, str]):
        self.__value = str(v)
        self.possible_values = []

        for cell in chain(self.row, self.col, self.square):
            if v in cell.possible_values:
                cell.possible_values.remove(v)

    @property
    def row(self) -> Tuple[Cell]:
        return self.__board.rows[self.__row_i]

    @property
    def col(self) -> Tuple[Cell]:
        return self.__board.cols[self.__col_i]

    @property
    def indexes(self) -> Tuple[int, int]:
        return self.__row_i, self.__col_i

    @property
    def square(self) -> Tuple[Cell]:
        if not self.__square:
            square_size = int(sqrt(len(self.row)))

            first_row = int(self.__row_i / square_size) * square_size
            last_row = first_row + square_size

            first_col = int(self.__col_i / square_size) * square_size
            last_col = first_col + square_size

            s = []
            for r in range(first_row, last_row):
                for c in range(first_col, last_col):
                    s.append(cast(Cell, self.__board.rows[r][c]))

            self.__square = tuple(s)

        return self.__square

    def __eq__(self, other: Union[int, str, Cell]) -> bool:
        if type(other) is Cell:
            other = other.value

        return self.__value == str(other)

    def __repr__(self) -> str:
        return str(self.value)

    def is_empty(self) -> bool:
        return self.value == e

    def can_fill(self, value: int) -> bool:
        return value in self.possible_values

    def update_possible_values(self) -> None:
        self.possible_values = []

        if self.is_empty():
            for digit in self.__board.digits:
                if digit not in self.row and digit not in self.col and digit not in self.square:
                    self.possible_values.append(digit)


class Board:
    def __init__(self, values=None):
        board_size = len(values)

        self.__board = tuple(
            tuple(Cell(self, row_index, col_index, str(values[row_index][col_index]))
                  for col_index in range(board_size))
            for row_index in range(board_size))

        self.__cols = tuple(
            tuple(cast(Cell, row[col]) for row in self.rows) for col in range(len(self.__board))
        )
        self.__cells = tuple(cell for row in self.rows for cell in row)

        for cell in self.cells:
            cell.update_possible_values()

    @property
    def rows(self) -> Tuple[Tuple[Cell]]:
        return self.__board

    @property
    def cols(self) -> Tuple[Tuple[Cell]]:
        return self.__cols

    @property
    def cells(self) -> Tuple[Cell]:
        return self.__cells

    @property
    def digits(self) -> range:
        return range(1, 10)

    def __repr__(self) -> str:
        return '\n'.join(
            ''.join(str(cell) for cell in row) for row in self.rows
        )

    def at(self, row: int, col: int) -> Cell:
        return self.rows[row][col]

    def copy(self) -> Board:
        values = [[cell.value for cell in row] for row in self.rows]

        copied = Board(values)

        return copied

    def is_solvable(self) -> bool:
        return all((not cell.is_empty()) or len(cell.possible_values) > 0 for cell in self.cells)

    def is_complete(self) -> bool:
        return all(not cell.is_empty() for cell in self.cells)
