# Shuffle an Array
# 当然可以直接调用random.shuffle()
# 看了一下random.shuffle()的实现方法，学习了一下Fisher–Yates shuffle
# Fisher–Yates shuffle：O(n)，每次从当前排列中随机选择一个元素，放到当前列的最后（最前）

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.s = nums.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # random.shuffle(self.s)
        for i in reversed(range(1, len(self.s))):
            pick = random.randint(0, i)
            self.s[pick], self.s[i] = self.s[i], self.s[pick]
        return self.s


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()