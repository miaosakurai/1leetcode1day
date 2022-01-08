class Solution:
    def rotate_temp(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. use tmp nums
        # T: O(n), S:O(n)
        k = k % len(nums)
        tmp_nums = nums[-k:]
        nums[k+1:] = nums[:-k]
        nums[:k+1] = tmp_nums[-k:]

    def rotate_TLE(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # rotate step by step (TLE)
        # T: O(n^2), S:O(1)
        k = k % len(nums)
        for i in range(k):
            first = nums[-1]
            nums[1:] = nums[:-1]
            nums[0] = first
    
    def rotate_reverse(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # A + B -> B + A
        # A + B -> rot(rot(A)+rot(B)) = B + A
        # T: O(n), S: O(1)
        def rev(l, start, end):
            while start<end:
                l[start], l[end] = l[end], l[start]
                start += 1
                end -= 1
        n = len(nums)
        k %= n
        rev(nums, 0, n-k-1)
        rev(nums, n-k, n-1)
        rev(nums, 0, n-1)