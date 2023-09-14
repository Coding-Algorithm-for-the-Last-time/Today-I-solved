class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for s in word:
            child = curr.children.get(s)
            if not child:
                child = TrieNode()
                curr.children[s] = child
            curr = child
        curr.end = True

    def _search_node(self, word: str) -> TrieNode | None:
        curr = self.root
        for s in word:
            curr = curr.children.get(s)
            if not curr:
                return None
        return curr

    def search(self, word: str) -> bool:
        curr = self._search_node(word)
        return False if not curr else curr.end

    def startsWith(self, prefix: str) -> bool:
        return bool(self._search_node(prefix))


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
