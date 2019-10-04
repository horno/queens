import sys
import subprocess
  
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
  
def solveQueenRecursive(board, col, N, it): 
      
    if col >= N: 
        return True, 0
  
    for i in range(N): 
  
        if fits(board, i, col, N): 
              
            board[i][col] = 1
            
            

            if solveQueenRecursive(board, col + 1, N, it + 1)[0]: 
                return True, 0
  
            board[i][col] = 0
    print(it) 
   # if it%1 == 0:
    subprocess.call("./subprocess.sh")            
    printSol(board, N)
    print("\n")
    
    return False, 0
  
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

    if not solveQueenRecursive(board, 0, N, 0)[0]: 
        print ("Solution does not exist") 
        return False
  
    printSol(board, N) 
    return True
  
solveQueen() 
