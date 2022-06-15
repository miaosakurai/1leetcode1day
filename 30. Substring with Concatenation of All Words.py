class Solution:
    # sliding window
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        lw = len(words[0])
        nw = len(words)

        for i in range(lw):
            counter = Counter(words)
            j=i
            while i<len(s)-lw*nw+1:
                if s[j:j+lw] not in counter: # start from right next
                    i=j+lw
                    j=i
                    counter = Counter(words)
                elif counter[s[j:j+lw]]<=0: # move left
                    counter[s[i:i+lw]]+=1
                    i+=lw
                else:
                    counter[s[j:j+lw]]-=1 # move right
                    j+=lw
                    
                # print(counter, s[i:j], i, j)
                if sum(counter.values())==0:
                    res.append(i)
                    counter[s[i:i+lw]]+=1
                    i+=lw
        return res
        
class Solution:
    # TLE
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        for i in range(len(s)):
            if self.found(s[i:], words):
                res.append(i)
        return res
            
    def found(self, s, words):
        if len(words)==0: return True
        if len(s)<sum([len(w) for w in words]): return False
        # match first word
        for i,w in enumerate(words):
            if s[:len(w)]==w:
                if self.found(s[len(w):], words[:i]+words[i+1:]):
                    return True
        return False
        