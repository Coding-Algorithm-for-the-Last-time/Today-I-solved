class Tree:
    def __init__(self, key: str | None = None, data: str | None = None, child={}):
        self.key = key
        self.data = data
        self.child = child or {}


class Trie:
    def __init__(self):
        self.head = Tree()

    def insert(self, word: str) -> None:
        curr = self.head
        for s in word:
            child = curr.child.get(s)
            if not child:
                child = Tree(s)
                curr.child[s] = child
            curr = child
        curr.data = word

    def search(self, word: str) -> bool:
        curr = self.head
        for s in word:
            curr = curr.child.get(s)
            if not curr:
                return False
        if not curr.data:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for s in prefix:
            curr = curr.child.get(s)
            if not curr:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
