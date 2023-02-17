#!/usr/bin/python3
"""Rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotates 2D matrox 90 degrees clockwise
    Matrix is edited in-place
    args:
        matrix
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # save topleft value
            topleft = matrix[top][left + 1]
            # move bottom left to top left
            matrix[top][left + 1] = matrix[bottom - i][left]
            # move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # move top left to topleft
            matrix[top + i][right] = topleft
        right -= 1
        left += 1
