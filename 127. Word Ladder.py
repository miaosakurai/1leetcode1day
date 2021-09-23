# 方法：BFS找到从起点到终点的路径，每次从word list中找到当前词的相邻词并删除
# 如何找相邻词？
# ladderLength1 (TLE): 遍历word list，逐个判断是不是当前词的相邻词 O(n^2)
# ladderLength2 (AC): 生成当前词的所有可能相邻词，判断每个是否在word list中 O(n*26*k)
# word list先转换为set节省判断in的时间

class Solution:
    def ladderLength1(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0
        d = 1  # depth
        q = [beginWord]
        if beginWord in wordList:
            wordList.pop(beginWord)
        while len(q)>0:
            next_q = []
            for cur in q:
                if cur==endWord: return d
                j = 0
                while len(wordList)>0 and j<len(wordList):
                    if self.is_adj(wordList[j], cur):
                        next_q.append(wordList.pop(j))
                    else:
                        j+=1
            d += 1
            q = next_q
        return 0
                
                    
    def is_adj(self, w, cur):
        if len(w)!=len(cur): return False
        found_diff = False
        for i in range(len(w)):
            if w[i]!=cur[i]:
                if not found_diff:
                    found_diff = True
                else:
                    return False
        if found_diff:
            return True
        else:
            return False


    def ladderLength2(self, beginWord: str, endWord: str, wordList) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        d = 1  # depth
        q = [beginWord]
        if beginWord in wordList:
            wordList.remove(beginWord)
        while len(q)>0:
            next_q = []
            for cur in q:
                if cur==endWord: return d
                for i in range(len(cur)):
                    for c in [chr(i) for i in range(97, 123)]:
                        tmp_w = cur[:i]+c+cur[i+1:]
                        if tmp_w in wordList:
                            wordList.remove(tmp_w)
                            next_q.append(tmp_w)
            d += 1
            q = next_q
        return 0
