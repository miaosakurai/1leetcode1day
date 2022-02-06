class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 分别记录第一个数（长度为1队列）和第二个数（长度为2队列）
        n1 = float('inf')  # nums最小值（第一个数最小值）
        n2 = float('inf')  # 第二个数最小值
        for n in nums:
            if n<=n1:
                n1 = n
            elif n<=n2:
                n2 = n
            else:
                return True
        return False

    # MLE -> 只需要记录两个队列，长度1队列和长度2队列
    def increasingTriplet_mle(self, nums: List[int]) -> bool:
        # 队列里有一个：
            # 大于最后一个：加入
            # 小于最后一个：替换
        # 队列里有两个：
            # 大于最后一个：true
            # 大于倒数第二，小于最后一个：替换最后一个
            # 小于倒数第二：创建新stack
        stacks = [[nums[0]]]
        for n in nums[1:]:
            new_stacks = []
            for stack in stacks:
                if len(stack)==1:
                    if n>stack[0]:
                        stack.append(n)
                    else:
                        stack[0]=n
                elif len(stack)==2:
                    if n>stack[-1]:
                        return True
                    elif n<=stack[-1] and n>stack[-2]:
                        stack[-1]=n
                    else:
                        new_stacks.append([n])
            stacks.extend(new_stacks)
        return False