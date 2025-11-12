from collections import deque
from typing import List


class shortestPath:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]== 1 or grid[n-1][n-1]==1:
            return -1
        # Queue<int []> queue= new LinkedList<>();
        queue=  deque()
        queue.append((0,0,1))
        visited=[[False]*n for _ in range(n)]
        visited[0][0]=True


        while queue:

            cRow,cCol,cTime=queue.popleft()
            if cRow==n-1 and cCol==n-1:
                return cTime
            dir= [
            (-1, -1), (-1, 0), (-1, 1),
            (0, 1), (1, 1), (1, 0),
            (1, -1), (0, -1)
            ]
            for r, c in dir:
                nRow=cRow+r
                nCol=cCol+c
                if nRow>=0 and nCol>=0 and nCol<n and nRow<n and not visited[nRow][nCol] and grid[nRow][nCol] == 0:
                    visited[nRow][nCol]= True
                    queue.append((nRow,nCol,cTime+1))


        return -1








