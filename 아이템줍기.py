def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0 for j in range(102)]  for i in range(102)]
    
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*x1, 2*x2+1):
            for j in range(2*y1, 2*y2+1):
                board[i][j] = 1
                
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*x1+1, 2*x2):
            for j in range(2*y1+1, 2*y2):
                board[i][j] = 0
                
    chX, chY, iX, iY = 2*characterX, 2*characterY, 2*itemX, 2*itemY
    
    stack = [[0, chX, chY]]
    while stack:
        ans, chX, chY = stack.pop(0)
        board[chX][chY] = -1
        
        if board[iX][iY] < 0:
            return ans//2
        
        for idx, idy in [[-1,0], [1,0], [0, -1], [0, 1]]:
            if board[chX+idx][chY+idy] > 0:
                stack.append([ans+1, chX+idx, chY+idy])
