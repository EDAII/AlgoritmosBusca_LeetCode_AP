from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["$"] = word  # marcador de palavra completa

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return
            next_node = node[ch]

            #encontramos palavra
            if "$" in next_node:
                result.append(next_node["$"])
                del next_node["$"]  # evita duplicados

            #visitado
            board[r][c] = "#"
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            board[r][c] = ch  # restaura

            # remove ramo vazio da trie
            if not next_node:
                node.pop(ch)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return result
