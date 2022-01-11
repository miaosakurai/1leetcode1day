class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 两两之和加入counter
        # T: O(n^2), S: O(n^2)
        ct1, ct2 = Counter(), Counter()
        n = len(nums1)
        res = 0
        for i in range(n):
            for j in range(n):
                ct1[nums1[i]+nums2[j]]+=1
                ct2[nums3[i]+nums4[j]]+=1
        for k1 in ct1:
            for k2 in ct2:
                if k1+k2==0:
                    res += ct1[k1] * ct2[k2]
        return res

    def fourSumCount2(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 6个counter
        # T: O(n^2), S: O(n^2)
        ct1, ct2, ct3, ct4 = Counter(nums1), Counter(nums2), Counter(nums3), Counter(nums4)
        ct5, ct6 = Counter(), Counter()
        res = 0
        for k1 in ct1:
            for k2 in ct2:
                ct5[k1+k2] += ct1[k1] * ct2[k2]
        for k3 in ct3:
            for k4 in ct4:
                ct6[k3+k4] += ct3[k3] * ct4[k4]
        for k5 in ct5:
            for k6 in ct6:
                if k5+k6==0:
                    res += ct5[k5] * ct6[k6]
        return res

    def fourSumCount3(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 1个counter
        # T: O(n^2), S: O(n^2)
        ct1 = Counter(a+b for a in nums1 for b in nums2)
        return sum(ct1[-c-d] for c in nums3 for d in nums4)