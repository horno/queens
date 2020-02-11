#!/usr/bin/env python3
import sys

class State:

    def __init__(self, N, initial_y_queen):
        self.N = N
        self.queens = {}
        self.y_axis = {}
        self.initial_move(initial_y_queen)

    def initial_move(self, y):
        self.position((0, y))

    def knight_moves(self, pos):
        # mov = lambda ops: lambda point: ((point[0] + ops[0](1)) % self.N, (point[1] + ops[1](2)) % self.N)
        # res = list(map(lambda x: x((1, 2)), map(mov, ops)))
        move = lambda point, mov: ((point[0] + mov[0]) % self.N, (point[1] + mov[1]) % self.N)
        opers = lambda x: abs(x), lambda x: -abs(x)
        ops = [(i, j) for i in opers for j in opers]
        res = [move(pos, (op1(1), op2(2))) for op1, op2 in ops] + [move(pos, (op1(2), op2(1))) for op1, op2 in ops]

        return list(set(res))

    def position(self, pos):
        self.queens[pos[0]] = pos[1]
        self.y_axis[pos[1]] = 'Q'

    def diagonal_collision(self, pos):
        for queen_x, queen_y in self.queens.items():
            if abs(queen_x - pos[0]) == abs(queen_y - pos[1]):
                return True
        return False

    def available_position(self, pos):
        if pos[1] in self.y_axis or pos[0] in self.queens or self.diagonal_collision(pos):
            return False
        return True

    def move_along(self):
        for key, value in self.queens.items():
            pos = (key, value)
            moves = self.knight_moves(pos)
            for move in moves:
                if self.available_position(move):
                    self.position(move)
                    return True
        return False

    def queens_placed(self):
        return len(self.queens)

    def print_matrix(self, matrix):
        for i in range(self.N):
            for j in range(self.N):
                print(matrix[i][j], end="  ")
            print('')

    def print_state(self):
        board = [['_' for col in range(self.N)] for row in range(self.N)]
        for key, value in self.queens.items():
            board[value][key] = "X"
        self.print_matrix(board)
        print(self.queens)
        print(self.y_axis)
        print()


def main():
    if len(sys.argv) != 2:
        print(" Use:\n\tpython3 horse_approach.py N_of_NxN_table")
        sys.exit()
    N = int(sys.argv[1])

    for i in range(N):
        state = State(N, i)
        while state.move_along():
            state.print_state()
        print("Achieved = " + str(state.queens_placed()))
        '''if state.queens_placed() == N:
            break'''


if __name__ == '__main__':
    main()
