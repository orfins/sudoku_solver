from time import time

from strategies import guess_fills
from structures import Board
from tests.boards import board_values_by_difficulty


def main():
    for difficulty in board_values_by_difficulty:
        board = Board(board_values_by_difficulty[difficulty]['problem'])

        start = time()
        solved = guess_fills(board)
        end = time()
        print(difficulty, solved, end - start)


if __name__ == '__main__':
    main()
