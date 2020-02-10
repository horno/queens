#!/usr/bin/env python3
import sys



'''
    First approach. Noticed a problem in the knight moves, there are the height ones (+-1,+-2)
    and the length ones (+-2,+-1). You can reach all the solutions if both of them are used, 
    if either of those is excluded there is no way to reach all the solutions. At the same 
    time, if both of them are used we can't asure that the movement won't result in a diagonal
    collition, wich does not happens if we use only one of them. This dichotomy must be resolved
    to continue with the approach.
'''

class State:

    def __init__(self, N):
        self.N = N
        self.queens = {}
        self.y_axis = {}
    
    def __init__(self,N,initial_y_queen):
        self.N = N
        self.queens = {}
        self.y_axis = {}
        self.initial_move(initial_y_queen)

    def initial_move(self, y):
        self.position((0,y))

    def knight_moves(self, pos):
        '''moves = [((pos[0]+2)%self.N,(pos[1]+1)%self.N),((pos[0]+2)%self.N,(pos[1]-1)%self.N),
                ((pos[0]-2)%self.N,(pos[1]+1)%self.N),((pos[0]-2)%self.N,(pos[1]-1)%self.N),
                ((pos[0]+1)%self.N,(pos[1]+2)%self.N),((pos[0]+1)%self.N,(pos[1]-2)%self.N),
                ((pos[0]-1)%self.N,(pos[1]+2)%self.N),((pos[0]-1)%self.N,(pos[1]-2)%self.N)] 
        '''
        moves = [((pos[0]+1)%self.N,(pos[1]+2)%self.N),((pos[0]+1)%self.N,(pos[1]-2)%self.N),
                ((pos[0]-1)%self.N,(pos[1]+2)%self.N),((pos[0]-1)%self.N,(pos[1]-2)%self.N)] 

        return moves

    def position(self, pos):
        self.queens[pos[0]] = pos[1]
        self.y_axis[pos[1]] = 'Q'


    def avaliable_position(self, pos):
        if pos[1] in self.y_axis or pos[0] in self.queens:
            return False
        return True

    def move_along(self):        
        for key, value in self.queens.items():
            pos = (key,value)
            moves = self.knight_moves(pos)
            for move in moves:
                if self.avaliable_position(move):
                    self.position(move)
                    return True
        return False
    
    def queens_placed(self):
        return len(self.queens)

    def print_matrix(self, matrix):
        for i in range(self.N):
            for j in range(self.N):
                print(matrix[i][j], end= "  ")
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
        state = State(N,i)
        while state.move_along():
            state.print_state()
        print("Achieved = " + str(state.queens_placed()))            
        '''if state.queens_placed() == N:
            break'''


if __name__ == '__main__':
    main()






