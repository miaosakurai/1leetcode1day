class Solution:
    # two pointer
    def longestDecomposition1(self, text: str) -> int:
        n = len(text)
        i = 0
        res = 0
    
        while i in range(n//2):
            j = i
            while j in range(n//2):
                if not self.match(text, i, j):
                    j+=1
                else:
                    res+=2
                    break
            i = j+1
            
        if i==n/2: return res
        else: return res+1
    
    def match(self, text, l, r):
        # i -> len(text)-i+1
        n = len(text)
        if text[l:r+1] != text[n-r-1: n-l]:
            return False
        else:
            return True
        
    # 递归
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        if n==0: return 0
        elif n==1: return 1

        for i in range(n//2):
            if text[:i+1] == text[n-1-i:]:
                return 2 + self.longestDecomposition(text[i+1: n-1-i])
        return 1
    
        
Solution().longestDecomposition("ghiabcdefhelloadamhelloabcdefghi")