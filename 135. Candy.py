# Children with a higher rating get more candies than their neighbors.
# 1 2 3 4 -> 0 1 2 3
# 1 3 2 4 -> 0 1 0 1

# 相等的时候没有要求:
# [1,3,3,2,1] -> [1,2,3,2,1]
# [1,3,3,3,2,1] -> [1,2,1,3,2,1]

import numpy as np
class Solution:
    # 局部最低点=0，往两边扩展到局部最高点（局部最高点取max）
    # 找局部最低：除去以遍历元素的全局最低，先sort
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n<=1: return n
        indices = np.argsort(ratings).tolist()
        candies = [1 for i in range(n)]
        while len(indices)>0:
            local_min = indices.pop(0)
            for i in range(local_min+1, n):
                if ratings[i]>ratings[i-1]:
                    candies[i] = max(candies[i], candies[i-1]+1)
                else:
                    break
                if i in indices:
                    indices.remove(i)

            for i in reversed(range(local_min)):
                if ratings[i]>ratings[i+1]:
                    candies[i] = max(candies[i], candies[i+1]+1)
                else:
                    break
                if i in indices:
                    indices.remove(i)
        return sum(candies)

    # 优化：不需要从局部最低点出发，只要从左到右、从右到左检查两遍即可
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n<=1: return n
        candies = [1 for i in range(n)]

        for i in range(1, n):
            if ratings[i]>ratings[i-1]:
                candies[i] = candies[i-1]+1

        for i in reversed(range(n-1)):
            if ratings[i]>ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)

        return sum(candies)