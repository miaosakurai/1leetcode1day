class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
            
        if cur.endOfWord:
            return True
        else:
            return False
    
    def isConcatenated(self, word):
        if len(word)==0:
            return True
        cur = self.root
        
        for i, c in enumerate(word):
            if cur.endOfWord:
                if self.isConcatenated(word[i:]) or self.search(word[i:]):
                    return True
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return False
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # 1. 把所有词加入trie
        # O(n * l)
        trie = Trie()
        
        for w in words:
            if len(w)>0:
                trie.insert(w)
        
        results = []
        # 2. isConcatenated：出现completed word时，判断剩余部分isConcatenated
        for w in words:
            if len(w)>0 and trie.isConcatenated(w):
                results.append(w)
        return results
        