#!/usr/bin/env python3

import sys
import subprocess


n_sol = 0 
  
def printSol(board, N): 
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 
#        print("\n", end = " ")
        print() 
#    subprocess.call("./sleep.sh")  

def fits(board, row, col, N): 
  
    for i in range(col): 
        if board[row][i] == 1: 
            return False
  
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    for i, j in zip(range(row, N, 1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True
  
def solveQueenRecursive(board, col, N): 
    if col >= N: 
        return True
  
    for i in range(N): 
  
        if fits(board, i, col, N): 
              
            board[i][col] = 1
            
            

            if solveQueenRecursive(board, col + 1, N): 
                global n_sol
                n_sol += 1
                print(n_sol)
                printSol(board, N)
                print("\n") 
            board[i][col] = 0
    print(it) 
   # if it%1 == 0:
    subprocess.call("./subprocess.sh")            
    printSol(board, N)
    print("\n")
    
def solveQueen(): 
    
    if len(sys.argv) != 2:
        print(" Use:\n\tpython3 queens.py N_of_NxN_table")
        sys.exit()
    N = int(sys.argv[1])
    
    board = []

    for i in range(N):
        board.append([])
        for j in range(N):
            board[i].append(0)

    solveQueenRecursive(board, 0, N) 
    if n_sol == 0:
        print("There are no solutions")
    else:
        print("Solutions:", n_sol)



solveQueen() 
