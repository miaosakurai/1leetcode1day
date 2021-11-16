class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if int(len(nums)/k)!=len(nums)/k: return False
        c = Counter(nums)
        keys = sorted(c.keys())
        for key in keys[:-(k-1)]:
            if c[key]<0: return False
            if c[key]>0:
                for i in range(1, k):
                    if key+i not in c:
                        return False
                    else:
                        c[key+i]-=c[key]
            del c[key]
            
        for key in keys[-(k-1):]:
            if c[key]!=0:
                return False
        return True
    
    # 简化
    def isPossibleDivide_2(self, nums: List[int], k: int) -> bool:
        if int(len(nums)/k)!=len(nums)/k: return False
        c = Counter(nums)
        for i in sorted(c):
            if c[i]>0:
                for j in range(1, k):
                    c[i+j]-=c[i]
                    if c[i+j]<0: return False
            del c[i]
        return True