from copy import deepcopy
import time

class Solver:
    
    DEFAULT_BOARD = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]


    def board_is_legal(self, board):
        if len(board) != 9:
            return False

        for row in board:
            if len(row) != 9:
                return False

        return True


    def __init__(self, board=DEFAULT_BOARD):
        if self.board_is_legal(board):
            self.board = board
        
        else:
            self.board = Solver.DEFAULT_BOARD


    def print_board(self):
        i = 0
        j = 0
        print("------------------------- \n")

        for row in self.board:
            i += 1
            j = 0
            print("|", end=" ")
            for col in row:
                j +=1
                print(col, end=" ")
                if j % 3 == 0:
                    print("|", end=" ")
                
                if j == 9:
                    print("\n")

            if i % 3 == 0:
                print("------------------------- \n")
            

    def num_is_legal(self, y, x, n):
        for i in range(0, 9):
            if self.board[y][i] == n:
                return False

        for i in range(0, 9):
            if self.board[i][x] == n:
                return False

        # check 3x3 subgrid of n
        x_sub_grid = (x // 3) * 3
        y_sub_grid = (y // 3) * 3

        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[y_sub_grid + i][x_sub_grid + j] == n:
                    return False

        return True

    
    def is_goal(self):
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        
        return True

    def solve(self):
        
        if self.is_goal():
            return True

        snapshot = deepcopy(self.board) 

        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    for n in range(1, 10):
                        if self.num_is_legal(y, x, n):
                            self.board[y][x] = n
                            result = self.solve()
                        
                            if result:
                                return True
                            else:
                                self.board = deepcopy(snapshot)

                    return False

    def solve_and_print(self):
        time_start = time.time()
        self.solve()
        time_end = time.time()
        print("SOLUTION:\n")
        self.print_board()
        print(f"Solved in {(time_end - time_start):.2f} seconds")
        




if __name__ == "__main__":
    test_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
    s = Solver(test_board)
    s.solve_and_print()
    
