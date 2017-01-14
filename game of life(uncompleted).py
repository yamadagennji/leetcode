
def gameOfLife( board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    n=len(board)
    m=len(board[0])
    if len(board)==0:
        return board
    aa=[]
    bb=[]#zhunbeiji
    for a in range(0,len(board[0])):
        aa.append(0)
    for b in range(0,len(board)):
        bb.append(list(aa))
    bb[0][0]=board[0][1]+board[1][1]+board[1][0]
    bb[n-1][0]=board[n-2][0]+board[n-1][1]+board[n-2][1]
    bb[n-1][m-1]=board[n-2][m-1]+board[n-1][m-2]+board[n-2][m-2]
    bb[0][m-1]=board[0][m-2]+board[1][m-1]+board[1][m-2]
    
    for c in range(1,n+1):
        bb[c][0]=bb[]
    
    print(bb)

abc=gameOfLife([[1,0,1],[1,1,0]])
