# 字典树用于动态单词查询
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_leaf = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_leaf = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)
                
    def dfs(self, root, word):
        if len(word)==0:
            if root.is_leaf:
                return True
            else:
                return False
        c = word[0]
        if c=='.':
            res = False
            for child in root.children:
                res = res or self.dfs(root.children[child], word[1:])
            return res
        elif c in root.children:
            return self.dfs(root.children[c], word[1:])
        else:
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)