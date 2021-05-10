from collections import defaultdict, Counter

# 两个list的交集，保留重复
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 分别统计两个list的字符频率，都出现过的取min -> 用Counter统计频率 
        # d1 = defaultdict(int)
        # for i in range(len(nums1)):
        #     d1[nums1[i]]+=1
        # d2 = defaultdict(int)
        # for i in range(len(nums2)):
        #     d2[nums2[i]]+=1
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        
        res = []
        for k in d1:
            if k in d2:
                for t in range(min(d1[k], d2[k])):
                    res.append(k)
        return res

