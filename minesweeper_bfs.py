"""
T.C = O(m*n) where m is the rows and n is the col of the board
S.C = O(m*n) where m is the rows and n is the col of the board
"""
from queue import deque


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if len(board) == 0:
            return board
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        m = len(board)
        n = len(board[0])
        directions = [[0, 1], [-1, 1], [-1, 0],
                      [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1]]
        queue = deque()
        queue.append((click[0], click[1]))
        board[click[0]][click[1]] = "B"

        while queue:
            curr = queue.popleft()
            count = self.countMines(board, curr[0], curr[1])
            if count == 0:
                for dir in directions:
                    newRow = curr[0] + dir[0]
                    newCol = curr[1] + dir[1]
                    if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n and board[newRow][newCol] == "E":
                        queue.append((newRow, newCol))
                        board[newRow][newCol] = "B"
            else:
                board[curr[0]][curr[1]] = str(count)

        return board

    def countMines(self, board, i, j):
        count = 0
        directions = [[0, 1], [-1, 1], [-1, 0],
                      [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1]]
        for dir in directions:
            newRow = i + dir[0]
            newCol = j + dir[1]
            if newRow >= 0 and newRow < len(board) and newCol >= 0 and newCol < len(board[0]) and board[newRow][newCol] == "M":
                count += 1
        return count
