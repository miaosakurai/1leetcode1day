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

    class TrieNode:
        def __init__(self):
            self.is_leaf = False
            self.children = defaultdict(TrieNode)
        
    class Trie:
        def __init__(self):
            self.root = TrieNode()
        
        def addWords(self, word):
            node = self.root
            for c in word:
                node = node.children[c]
            node.is_leaf=True
            
        
    class Solution:
        # 把words存入词典树，同时遍历词典树和board
        def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
            m, n = len(board), len(board[0])
            res = set()
            trie = Trie()
            for w in words:
                trie.addWords(w)
            for i in range(m):
                for j in range(n):
                    self.dfs(board, i, j, "", trie.root, res)
            return list(res)

        def dfs(self, board, i, j, path, node, res):
            m, n = len(board), len(board[0])
            if i>=m or i<0 or j>=n or j<0:
                return 

            c = board[i][j]
            node = node.children.get(c)
            if not node:
                return
            if node.is_leaf:
                res.add(path+c)
                
            board[i][j]="#"
            self.dfs(board, i+1, j, path+c, node, res)
            self.dfs(board, i-1, j, path+c, node, res)
            self.dfs(board, i, j+1, path+c, node, res)
            self.dfs(board, i, j-1, path+c, node, res)
            board[i][j]=c
