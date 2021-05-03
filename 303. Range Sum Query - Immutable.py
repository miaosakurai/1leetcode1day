## Question
#  Return sum between left and right when call the sumRange function
#  Your NumArray object will be instantiated and called as such:
#  obj = NumArray(nums)
#  param_1 = obj.sumRange(left,right)

# 1-d dp
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dp = [0 for i in range(len(nums)+1)]
        for i in range(1, len(self.dp)):
            self.dp[i] = self.dp[i-1]+nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right+1]-self.dp[left]
        
# bf
class NumArrayBF:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])

    # def sumRange(self, left: int, right: int) -> int:
    #     sum = self.nums[left]
    #     for i in range(left+1, right+1):
    #         sum += self.nums[i]
    #     return sum


