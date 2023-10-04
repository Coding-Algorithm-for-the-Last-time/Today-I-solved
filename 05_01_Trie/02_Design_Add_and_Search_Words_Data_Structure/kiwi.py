class Tree:
    def __init__(self, children: dict, is_end: bool):
        self.children = children
        self.is_end = is_end


class WordDictionary:
    def __init__(self):
        self._tree: Tree = Tree({}, False)

    def addWord(self, word: str) -> None:
        tree = self._tree
        for s in word:
            if s not in tree.children:
                tree.children[s] = Tree({}, False)
            tree = tree.children[s]
        tree.is_end = True

    def search(self, word: str, tree: Tree = None) -> bool:
        if not tree:
            tree = self._tree

        if not (word and tree.children):
            return not word and tree.is_end

        if word[0] == ".":
            for child in tree.children.values():
                if self.search(word[1:], child):
                    return True
            return False

        if word[0] not in tree.children:
            return False

        return self.search(word[1:], tree.children[word[0]])
