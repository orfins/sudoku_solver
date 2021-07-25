from time import time

from strategies import guess_fills
from structures import Board
from tests.boards import board_values_by_difficulty


def main():
    # for difficulty in board_values_by_difficulty:
    #     board = Board(board_values_by_difficulty[difficulty]['problem'])
    #
    #     start = time()
    #     solved = guess_fills(board)
    #     end = time()
    #     print(difficulty, solved, end - start)

    debug=False

    from tensorflow.keras.preprocessing.image import img_to_array
    from tensorflow.keras.models import load_model
    model = load_model('/Users/or.f/PycharmProjects/sudoku_solver/output/digit_classifier.h5')

    import cv2
    p = '/Users/or.f/Desktop/b.png'
    # p = '/Users/or.f/Desktop/a.jpg'
    src = cv2.imread(p)
    from sudokurecognition.sudoku.puzzle import find_puzzle, extract_digit

    puzzleImage, warped = find_puzzle(src, debug)

    import numpy as np
    # initialize our 9x9 Sudoku board
    board = np.zeros((9, 9), dtype="int")
    # a Sudoku puzzle is a 9x9 grid (81 individual cells), so we can
    # infer the location of each cell by dividing the warped image
    # into a 9x9 grid
    stepX = warped.shape[1] // 9
    stepY = warped.shape[0] // 9
    # initialize a list to store the (x, y)-coordinates of each cell
    # location
    cellLocs = []

    # loop over the grid locations
    for y in range(0, 9):
        # initialize the current list of cell locations
        row = []
        for x in range(0, 9):
            # compute the starting and ending (x, y)-coordinates of the
            # current cell
            startX = x * stepX
            startY = y * stepY
            endX = (x + 1) * stepX
            endY = (y + 1) * stepY
            # add the (x, y)-coordinates to our cell locations list
            row.append((startX, startY, endX, endY))

            # crop the cell from the warped transform image and then
            # extract the digit from the cell
            cell = warped[startY:endY, startX:endX]
            digit = extract_digit(cell, debug)
            # verify that the digit is not empty
            if digit is not None:
                # resize the cell to 28x28 pixels and then prepare the
                # cell for classification
                roi = cv2.resize(digit, (28, 28))
                roi = roi.astype("float") / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                # classify the digit and update the Sudoku board with the
                # prediction
                pred = model.predict(roi).argmax(axis=1)[0]
                board[y, x] = pred
        # add the row to our cell locations
        cellLocs.append(row)

    # solve
    b = Board(board)
    print(b)
    guess_fills(b)

    # loop over the cell locations and board
    for (cellRow, boardRow) in zip(cellLocs, b.rows):
        # loop over individual cell in the row
        for (box, digit) in zip(cellRow, boardRow):
            # unpack the cell coordinates
            startX, startY, endX, endY = box
            # compute the coordinates of where the digit will be drawn
            # on the output puzzle image
            textX = int((endX - startX) * 0.33)
            textY = int((endY - startY) * -0.2)
            textX += startX
            textY += endY
            # draw the result digit on the Sudoku puzzle image
            cv2.putText(puzzleImage, str(digit), (textX, textY),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
    # show the output image
    cv2.imshow("Sudoku Result", puzzleImage)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
