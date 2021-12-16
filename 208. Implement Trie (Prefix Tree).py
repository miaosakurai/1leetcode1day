class TrieNode:
    def __init__(self):
        self.is_leaf = False
        self.children = defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_leaf = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node:
                return False
        if node.is_leaf:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            if not node:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)