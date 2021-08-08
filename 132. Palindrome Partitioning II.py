class Solution:
    # TLE
    def minCut_TLE(self, s: str) -> int:
        # cut[i]: 0~i之间的最小cut
        # cut[i] = cut[j]+1 (0<=j<=i, j~i是回文)
        cut = [i for i in range(len(s))]
        for i in range(1, len(s)):
            cut[i] = cut[i-1]+1
            if self.isPalindrome(s, 0, i):
                cut[i] = 0
            else:
                for j in range(1, i):
                    if self.isPalindrome(s, j, i):
                        cut[i] = min(cut[i], cut[j-1]+1)
        print(cut)
        return cut[-1]
    
    def isPalindrome(self, s, j, i):
        while j<i:
            if s[j]!=s[i]:
                return False
            j+=1
            i-=1
        return True
    
    '''
    判断回文有大量重复计算，先算好避免TLE
    isPalindrome[l][r] = (s[l]==s[r]) and isPalindrome[l+1][r-1]
    '''
    def minCut(self, s: str) -> int:
        cut = [i for i in range(len(s))]
        isPalindrome = [[True for j in range(len(s))] for i in range(len(s))]
        for r in range(1, len(s)):
            for l in range(r):
                isPalindrome[l][r] = (s[l]==s[r]) and isPalindrome[l+1][r-1]

        for i in range(1, len(s)):
            cut[i] = cut[i-1]+1
            if isPalindrome[0][i]:
                cut[i] = 0
            else:
                for j in range(1, i):
                    if isPalindrome[j][i]:
                        cut[i] = min(cut[i], cut[j-1]+1)
        return cut[-1]
