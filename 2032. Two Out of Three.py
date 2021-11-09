class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        res = set()
        for num in nums1:
            if num in nums2 or num in nums3:
                res.add(num)
        for num in nums2:
            if num in nums1 or num in nums3:
                res.add(num)
        for num in nums3:
            if num in nums1 or num in nums2:
                res.add(num)
        return list(res)
    
    # 优化
    def twoOutOfThree2(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return s1 & s2 | s1 & s3 | s2 & s3