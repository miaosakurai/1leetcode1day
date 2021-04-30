## Question
# check if nums could become non-decreasing by modifying at most one element.
# Input: nums = [4,2,3]
# Output: true

# greedy
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nd_stack = [nums[0]]
        found_dec = False
        for i in range(1, len(nums)):
            if nums[i]<nd_stack[-1]:
                if not found_dec: # can use chance to modify
                    # greedy: 让栈顶的元素尽量小
                    # 2 4 3 -> 2 2 3 (nums[i]小于上个但不小于上上个，可以把上个改小)
                    if len(nd_stack)<2 or nd_stack[-2]<=nums[i]:
                        nd_stack[-1]=nums[i]
                        # nd_stack.append(nums[i])
                        found_dec = True
                    # 4 4 3 -> 4 4 4 (nums[i]同时小于上个和上上个，只能把这个改大)
                    else:
                        # nd_stack.append(nd_stack[-1])
                        found_dec = True
                else:
                    return False
            else:
                nd_stack.append(nums[i])
        return True
            
        