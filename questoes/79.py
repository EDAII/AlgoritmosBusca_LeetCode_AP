from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # toda palavra encontrada
            if i == len(word):
                return True

            # Se sair dos limites ou a letra não bater
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != word[i]):
                return False

            # Marca como visitado temporariamente
            temp, board[r][c] = board[r][c], "#"

            # Visita os vizinhos
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))

            # backtracking
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
