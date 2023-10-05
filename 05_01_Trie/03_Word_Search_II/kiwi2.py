class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie, res = {}, []
        ROW, COL = range(len(board)), range(len(board[0]))

        for word in words:
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur[""] = word

        def dfs(row, col, parent_trie):
            if row not in ROW or col not in COL:
                return
            char = board[row][col]
            if not char or char not in parent_trie:
                return
            trie = parent_trie[char]

            if "" in trie:
                res.append(trie[""])
                del trie[""]

            board[row][col] = ""
            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(row + r, col + c, trie)
            board[row][col] = char

            if not trie:
                del parent_trie[char]

        for row in ROW:
            for col in COL:
                dfs(row, col, trie)
        return res
