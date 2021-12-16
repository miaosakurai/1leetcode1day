import copy

class Solution:
    # TLE
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        for w in words:
            if self.search(board, w):
                res.append(w)
        return res
        
    def search(self, board, word):
        m, n = len(board), len(board[0])
        
        def dfs(w, i, j,):
            if w[0]!=board[i][j]:
                return False
            if len(w)==1:
                return True
            res = False
            board[i][j]="#"  
            if i+1<m:
                res = res or dfs(w[1:], i+1, j)
            if i-1>=0:
                res = res or dfs(w[1:], i-1, j)
            if j+1<n:
                res = res or dfs(w[1:], i, j+1)
            if j-1>=0:
                res = res or dfs(w[1:], i, j-1)
            board[i][j]=w[0]
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(word, i, j):
                    return True
    #     return False
        
    # def search(self, board, word):
    #     m, n = len(board), len(board[0])
        
    #     def dfs(w, i, j, visited):
    #         if visited[i][j]:
    #             return False
    #         visited[i][j]=True
    #         if w[0]!=board[i][j]:
    #             return False
    #         if len(w)==1:
    #             return True
    #         res = False
    #         if i+1<m:
    #             v = copy.deepcopy(visited)
    #             res = res or dfs(w[1:], i+1, j, v)
    #         if i-1>=0:
    #             v = copy.deepcopy(visited)
    #             res = res or dfs(w[1:], i-1, j, v)
    #         if j+1<n:
    #             v = copy.deepcopy(visited)
    #             res = res or dfs(w[1:], i, j+1, v)
    #         if j-1>=0:
    #             v = copy.deepcopy(visited)
    #             res = res or dfs(w[1:], i, j-1, v)

    #         return res
        
    #     for i in range(m):
    #         for j in range(n):
    #             visited = [[False for j in range(n)] for i in range(m)]
    #             if dfs(word, i, j, visited):
    #                 return True
    #     return False
                
## solution 2: Trie + dfs
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

## solution 2 优化：把已经找到的词 is_leaf = False 避免重复找
class Solution:
    # 把words存入词典树，同时遍历词典树和board
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        res = []
        trie = Trie()
        for w in words:
            trie.addWords(w)
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, "", trie.root, res)
        return res

    def dfs(self, board, i, j, path, node, res):
        if node.is_leaf:
            res.append(path)
            node.is_leaf = False
        m, n = len(board), len(board[0])
        if i>=m or i<0 or j>=n or j<0:
            return 
        c = board[i][j]
        node = node.children.get(c)
        if not node:
            return
        board[i][j]="#"
        self.dfs(board, i+1, j, path+c, node, res)
        self.dfs(board, i-1, j, path+c, node, res)
        self.dfs(board, i, j+1, path+c, node, res)
        self.dfs(board, i, j-1, path+c, node, res)
        board[i][j]=c
