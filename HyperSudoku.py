# A few test cases are provided in Test.py.

#1111111 (new branch)
# added this new line here
=======
#1111111 (new branch) (abc)
# added this line from master

# for 9x9 grid solver
class HyperSudoku:

    # @staticmethod
    # def valid_row(grid, row_index, val) -> bool:
    #     check_row = grid[row_index]
    #     if val in check_row:
    #         return False
    #     return True

    @staticmethod
    def valid_col(grid, col_index, val) -> bool:
        for curr_row_index in range(9):
            if grid[curr_row_index][col_index] == val:
                return False

        return True

    @staticmethod
    def valid_sub_grid(grid, row_index, col_index, val) -> bool:
        start_row_index = 3 * (row_index // 3)
        start_col_index = 3 * (col_index // 3)
        for i in range(start_row_index, start_row_index + 3):
            for j in range(start_col_index, start_col_index + 3):
                if val == grid[i][j]:
                    return False

        return True

    @staticmethod
    def valid_hyper_sudoku(grid, given_row_index, given_col_index,
                           given_val) -> bool:

        if (1 <= given_row_index <= 3) and (1 <= given_col_index <= 3):
            # start_row_value = 1
            # start_col_value = 1
            for i in range(1, 4):
                for j in range(1, 4):
                    if given_val == grid[i][j]:
                        return False

        elif (5 <= given_row_index <= 7) and (1 <= given_col_index <= 3):
            # start_row_value = 5
            # start_col_value = 1
            for i in range(5,8):
                for j in range(1,
                               4):
                    if given_val == grid[i][j]:
                        return False

        elif (1 <= given_row_index <= 3) and (5 <= given_col_index <= 7):
            # start_row_value = 1
            # start_col_value = 5
            for i in range(1,
                           4):
                for j in range(5,
                               8):
                    if given_val == grid[i][j]:
                        return False

        elif (5 <= given_row_index <= 7) and (5 <= given_col_index <= 7):
            # start_row_value = 5
            # start_col_value = 5
            for i in range(5,
                           8):
                for j in range(5,
                               8):
                    if given_val == grid[i][j]:
                        return False
        return True



    @staticmethod
    def solve(grid):
        """
        Input: An 9x9 hyper-sudoku grid with numbers [0-9].
                0 means the spot has no number assigned.
                grid is a 2-Dimensional array. Look at
                Test.py to see how it's initialized.

        Output: A solution to the game (if one exists),
                in the same format. None of the initial
                numbers in the grid can be changed.
                'None' otherwise.
        """

        # check if the grid is solvable

        for row_index in range(len(grid)):
            for col_index in range(len(grid)):
                current_value = grid[row_index][col_index]

                # value that wasn't enter
                if grid[row_index][col_index] == 0:

                    # store all the possible values in a set for the curr cell
                    possible_value = set()
                    for i in range(1, 10):
                        # check everything before adding the value
                        cond_1 = HyperSudoku.valid_col(grid, col_index, i)
                        cond_3 = HyperSudoku.valid_sub_grid(grid, row_index,
                                                            col_index,
                                                            i)
                        cond_4 = HyperSudoku.valid_hyper_sudoku(grid, row_index,
                                                                col_index,
                                                                i)

                        if i not in grid[row_index]:
                            possible_value.add(i)

                        elif cond_1 :
                            possible_value.add(i)

                        if cond_3:
                            possible_value.add(i)

                    for a_pos_val in possible_value:
                        grid[row_index][col_index] = a_pos_val
                        if HyperSudoku.solve(
                                grid) is not None:
                            return grid
                        else:
                            grid[row_index][col_index] = 0
                    return None

        return grid  # Update this to return correctly

    @staticmethod
    def printGrid(grid):
        """
        Prints out the grid in a nice format. Feel free
        to change this if you need to, it will NOT be 
        used in marking. It is just to help you debug.

        Use as:     HyperSudoku.printGrid(grid)
        """
        print("-" * 25)
        for i in range(9):
            print("|", end=" ")
            for j in range(9):
                print(grid[i][j], end=" ")
                if (j % 3 == 2):
                    print("|", end=" ")
            print()
            if (i % 3 == 2):
                print("-" * 25)
