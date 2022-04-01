class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count = k
        self.res = ""
        cur = []
        chars = ["a", "b", "c"]
        
        if k>3*2**(n-1):
            return ""
        
        def btrack(cur):
            if self.count<0:
                return
            if len(cur) == n:
                self.count -= 1
                if self.count==0:
                    self.res = "".join(cur)
                return
            for c in chars:
                if len(cur)==0 or c!=cur[-1]:
                    cur.append(c)
                    btrack(cur)
                    cur.pop()

        while self.count>0:
            btrack(cur)
        return self.res