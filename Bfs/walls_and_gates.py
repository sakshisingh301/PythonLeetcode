from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        row=len(rooms)
        col=len(rooms[0])
        INF = 2147483647
        queue=deque()
        for r in range(row):
            for c in range(col):
                if rooms[r][c]==0:
                    queue.append((r, c, 0))

        while queue:
            c_row, c_col, c_time=queue.popleft()
            dir =[(1,0), (-1,0), (0,1), (0,-1)]
            for r, c in dir:
                n_row=c_row+r
                n_col=c_col+c
                if n_row >= 0 and n_col >= 0 and n_row < row and n_col < col and rooms[n_row][n_col] == INF and rooms[n_row][n_col] != 0:
                    rooms[n_row][n_col]=c_time+1
                    queue.append((n_row,n_col,c_time+1))





