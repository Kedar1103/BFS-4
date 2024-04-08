"""
T.C = O(n*n) where n is the rows or cols of the board
S.C = O(n*n) where n is the rows or cols of the board
"""
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        if len(board) == 0:
            return -1
        n = len(board)
        moves = [0 for _ in range(n*n)]
        even = 0
        i = n - 1
        j = 0
        idx = 0

        while idx < n*n:
            print(f"i={i} j={j}")
            if board[i][j] == -1:
                moves[idx] = board[i][j]
            else:
                moves[idx] = board[i][j] - 1
            idx += 1
            if even % 2 == 0:
                j += 1
                if j == n:
                    i -= 1
                    j -= 1
                    even += 1
            else:
                j -= 1
                if j == -1:
                    i -= 1
                    j += 1
                    even += 1

        queue = deque()
        queue.append(0)
        moves[0] = -2
        ans = 0
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr == n*n - 1:
                    return ans
                for i in range(1, 7):
                    newIdx = curr + i
                    if newIdx < n*n:
                        if moves[newIdx] != -2:
                            if moves[newIdx] == -1:
                                queue.append(newIdx)
                            else:
                                queue.append(moves[newIdx])
                            moves[newIdx] = -2
            ans += 1
        return -1
