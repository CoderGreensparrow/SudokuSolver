"""
My implementation of an abstract sudoku board and a method of displaying it.
"""

class Sudoku:
    def __init__(self, numbers: list[list[int | None]] = None):
        """
        An abstract representation of a sudoku board by storing the numbers (or None) in a basic matrix.
        :param numbers: The numbers in a 9x9 grid. If None is given, an empty 9x9 board is generated.
        """
        if not numbers:
            numbers = [[None for j in range(9)] for i in range(9)]
        self.numbers: list[list[int | None], ...] = numbers

    def get_cell(self, pos: list[int, int]) -> int | None:
        """
        Get the value of a specific cell at specific coordinates.
        :param pos: The position of the cell. Format: [column from left starting at 1, row from top starting at 1]
        :return: The current value of the cell. Values: None (meaning empty), 1-9
        """
        assert 1 <= pos[0] <= len(self.numbers[0]), f"Column position {pos[0]} is invalid"
        assert 1 <= pos[1] <= len(self.numbers), f"Row position {pos[1]} is invalid"
        return self.numbers[pos[1] - 1][pos[0] - 1]

    def get_sudoku(self) -> list[list[int | None]]:
        """
        Get the whole sudoku matrix of numbers (or None).
        :return: Matrix of numbers (or None).
        """
        return self.numbers

    def set_cell(self, pos: list[int, int], value: int | None) -> None:
        """
        Set the value of a specific cell at specific coordinates.
        :param pos: The position of the cell. Format: [column from left starting at 1, row from top starting at 1]
        :param value: The new value of the cell. Values: None (meaning empty), 1-9
        :return: None
        """
        assert 1 <= pos[0] <= len(self.numbers[0]), f"Column position {pos[0]} is invalid"
        assert 1 <= pos[1] <= len(self.numbers), f"Row position {pos[1]} is invalid"
        assert 1 <= value <= 9 or value is None, f"New value {value} is invalid"
        self.numbers[pos[1] - 1][pos[0] - 1] = value

    def set_sudoku(self, numbers: list[list[int | None]]):
        """
        Set the whole sudoku matrix of numbers (or None).
        :param numbers: The numbers in a 9x9 grid.
        :return: None
        """
        self.numbers: list[list[int | None], ...] = numbers

    def validate(self) -> bool:
        """
        Return of the board is currently valid or not according to sudoku rules.
        :return: Boolean for validity
        """
        # 1. Validate rows
        for row in self.numbers:
            numbers_in_row = []
            for number in row:
                if number in numbers_in_row:
                    return False  # A number occurs at least twice in a row
                else:
                    numbers_in_row.append(number)
        # 2. Validate columns
        for col in range(len(self.numbers[0])):
            column = [self.numbers[col][i] for i in range(len(self.numbers))]  # get column
            # same logic
            numbers_in_column = []
            for number in column:
                if number in numbers_in_column:
                    return False  # A number occurs at least twice in a column
                else:
                    numbers_in_column.append(number)
        # 3. Check boxes
        boxes = [[(1, 1), (2, 1), (3, 1),
                  (1, 2), (2, 2), (3, 2),
                  (1, 3), (2, 3), (3, 3)]]