#!/usr/bin/env python3


class HorseState:

    def __init__(self, N, initial_y_queen):
        self.__last_queen = 0
        self.__N = N
        self.__queens = {}
        self.__y_axis = {}
        self._position(self.__last_queen, initial_y_queen)

    def get_queens(self):
        return self.__queens

    def get_y_axis(self):
        return self.__y_axis

    def get_last_queen(self):
        return self.__last_queen

    def _position(self, x, y):
        self.__queens[x] = y
        self.__y_axis[y] = 'Q'

    def moves(self):
        last_position = (self.__last_queen, self.__queens[self.__last_queen])
        return self.available_moves(knight_moves(last_position, self.__N))

    def move_to(self, new_position):
        x, y = new_position
        new_state = HorseState(self.__N, 0)
        new_state.__queens = self.__queens.copy()
        new_state.__y_axis = self.__y_axis.copy()
        new_state._position(x, y)
        new_state.__last_queen = x
        return new_state

    def print(self):
        import sys
        sys.stdout.write("+")
        for c in range(self.__N):
            sys.stdout.write("---+")
        sys.stdout.write("\n")
        # Draw board rows
        for r in range(self.__N):
            sys.stdout.write("|")
            # Draw column position
            for c in range(self.__N):
                if r in self.__queens and self.__queens[r] == c:  # If the row == to the value of the variable
                    sys.stdout.write(" X |")
                else:
                    sys.stdout.write("   |")
            sys.stdout.write("\n")
            # Middle lines
            sys.stdout.write("+")
            for c in range(self.__N):
                sys.stdout.write("---+")
            sys.stdout.write("\n")

    def available_moves(self, moves):
        if self.__N == len(self.__queens):
            return []
        res = []
        for move in moves:
            if move[0] not in self.__queens.keys() and move[1] not in self.__queens.values():
                res.append(move)
        return res


def knight_moves(pos, N):
    move = lambda point, mov: ((point[0] + mov[0]) % N, (point[1] + mov[1]) % N)
    opers = lambda x: abs(x), lambda x: -abs(x)
    ops = [(i, j) for i in opers for j in opers]
    res = [move(pos, (op1(1), op2(2))) for op1, op2 in ops] + [move(pos, (op1(2), op2(1))) for op1, op2 in ops]
    return list(set(res))


def main():
    state = HorseState(4, 0)
    print(state.moves())
    stack = [state]
    while len(stack) != 0:
        current = stack.pop()
        moves = current.moves()
        for move in moves:
            stack.append(current.move_to(move))
        if len(moves) == 0:
            current.print()


if __name__ == '__main__':
    main()
