class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0

    def add_word(self, word: str):
        cur = self
        for s in word:
            if s not in cur.children:
                cur.children[s] = Trie()
            cur = cur.children[s]
            cur.count += 1
        cur.is_end = True

    def remove_word(self, word: str):
        cur = self
        for s in word:
            cur = cur.children[s]
            cur.count -= 1
        cur.is_end = False


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = Trie()
        trie.count += 1
        for word in words:
            trie.add_word(word)

        res, visit = set(), set()

        def search(row, col, cur, word):
            if not (
                row in range(len(board))
                and col in range(len(board[0]))
                and cur.count > 0
                and (row, col) not in visit
                and board[row][col] in cur.children
            ):
                return

            word += board[row][col]
            cur = cur.children[board[row][col]]
            if cur.is_end:
                trie.remove_word(word)
                res.add(word)

            visit.add((row, col))
            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                search(row + r, col + c, cur, word)
            visit.remove((row, col))

        for i in range(len(board)):
            for j in range(len(board[0])):
                search(i, j, trie, "")
        return list(res)
