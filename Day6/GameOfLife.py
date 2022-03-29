class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(x,y,n,m):
            if x < 0 or y < 0 or x>=n or y >=m:
                return False
            else:
                return True
            
        n = len(board)
        m = len(board[0])
        next_state = [[0 for _ in range(m)] for _ in range(n)]
        
        dx=[-1,-1,-1,0,0,1,1,1]
        dy=[-1,0,1,-1,1,-1,0,1]
        
        for i in range(n):
            for j in range(m):
                count = 0
                curr = board[i][j]
                for k in range(8):
                    nR, nC = i+dx[k], j+dy[k]
                    if isValid(nR, nC, n, m) and board[nR][nC] == 1:
                        count += 1
                if curr == 1:
                    if count < 2:
                        next_state[i][j] = 0   # i.e, the cell will die
                    elif count == 2 or count == 3:
                        next_state[i][j] = 1   # i.e, lives on to the next generation
                    elif count >= 3:
                        next_state[i][j] = 0  #i.e, dies by over population
                elif curr == 0:
                    if count == 3:
                        next_state[i][j] = 1   #i.e, lives by reproduction
                    else:
                        next_state[i][j] = 0
                        
        for i in range(n):
            for j in range(m):
                board[i][j] = next_state[i][j]
        print(board)