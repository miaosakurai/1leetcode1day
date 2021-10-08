class Solution:
    def findKthBit1(self, n: int, k: int) -> str:
        sn = "0"
        for i in range(1, n):
            sn = sn + "1" + "".join([str(1-int(c)) for c in sn[::-1]])
        return sn[k-1]

    def findKthBit(self, n: int, k: int) -> str:
        if k==1:
            return "0"
        if k==2**(n-1):
            return "1"
        elif k<2**(n-1):
            return self.findKthBit(n-1, k)
        else:
            return "1" if self.findKthBit(n-1, 2**n-k)=="0" else "0"