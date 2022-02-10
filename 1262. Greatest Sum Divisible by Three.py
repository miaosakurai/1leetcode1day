class Solution:
    # 减法思维，算出总和的余数r，找到最小余数为r的组合
    # r = 1 or 2
    # if r==1: 两个r=2 or 一个r=1
    # if r==2: 两个r=1 or 一个r=2
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        r = total % 3
        if r == 0:
            return total
        nums.sort()
        r1, r2, r3 = 0, 0, 0   # where (r1+r2)%3==r, r3%3==r
        for i in range(len(nums)):
            if nums[i]%3==0:
                continue
            elif nums[i]%3==r:
                r3 = nums[i]
                break
            elif r1==0:
                r1 = nums[i]
            elif r2==0:
                r2 = nums[i]
            elif r1+r2<=nums[i]:
                break
        if r3==0:
            return total-r1-r2
        elif r1==0 or r2==0:
            return total-r3
        else:
            return total-min(r3, r1+r2)

    # 三种状态：当前余数为0,1,2的最大和
    def maxSumDivThree2(self, nums: List[int]) -> int:
        s0, s1, s2 = 0, 0, 0  # 当前余数为i的最大和
        for num in nums:
            if num % 3 == 0:
                s0, s1, s2 = s0+num, s1+num if s1>0 else s1, s2+num if s2>0 else s2
            elif num % 3 == 1:
                s0, s1, s2 = max(s0, s2+num) if s2>0 else s0, max(s1, s0+num), max(s2, s1+num) if s1>0 else s2
            else:
                s0, s1, s2 = max(s0, s1+num) if s1>0 else s0, max(s1, s2+num) if s2>0 else s1, max(s2, s0+num)
        return s0
    # 2的简化
    def maxSumDivThree3(self, nums: List[int]) -> int:
        r = [0] * 3  # r[i]: 当前余数为i的最大和
        for num in nums:
            for s in r[:]:  # copy of r
                r[(num+s)%3] = max(r[(num+s)%3], num+s)
        return r[0]