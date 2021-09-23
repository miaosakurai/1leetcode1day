from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordSet = set(wordList)
        path = [[beginWord]]
        while len(path)>0:
            adjs = set()
            adj_dict = defaultdict(list)
            pi = defaultdict(list)
            for i, p in enumerate(path):
                cur = p[-1]
                for j in range(len(cur)):
                    for c in [chr(i) for i in range(97, 123)]:
                        adj = cur[:j]+c+cur[j+1:] 
                        if adj in wordSet:
                            adjs.add(adj)
                            pi[i].append(adj)
                            adj_dict[adj].append(i)
                            
            wordSet -= adjs
            next_path = []
            if endWord in adj_dict:
                for i in adj_dict[endWord]:
                    next_path.append(path[i]+[endWord])
                return next_path
            
            for i in pi:
                if len(pi[i])>0:
                    for adj in pi[i]:
                        next_path.append(path[i]+[adj])
            path = next_path
            
        return []
                    
                    