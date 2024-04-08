"""
T.C = O(m*n) where m is the rows and n is the col of the board
S.C = O(m*n) where m is the rows and n is the col of the board
"""


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
        self.dfs(board, click[0], click[1], directions)
        return board

    def dfs(self, board, i, j, directions):
        # base
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "E":
            return

        # logic
        board[i][j] = "B"
        count = self.countMines(board, i, j)
        if count == 0:
            for dir in directions:
                newRow = i + dir[0]
                newCol = j + dir[1]
                self.dfs(board, newRow, newCol, directions)
        else:
            board[i][j] = str(count)

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
