class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # bottom-up
        pre_sum = triangle[-1]
        for i in reversed(range(len(triangle)-1)):
            cur_sum = []
            for j in range(len(triangle[i])):
                cur_sum.append(triangle[i][j]+min(pre_sum[j], pre_sum[j+1]))
            pre_sum = cur_sum
        return pre_sum[0]
                