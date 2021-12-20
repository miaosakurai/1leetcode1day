class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # sort
        # nums.sort()  # nlgn
        # res = 0
        # for i in range(len(nums)-1):
        #     res = max(res, nums[i+1]-nums[i])
        # return res
        
        # 🪣 桶排序
        # 最大值和最小值之间有n-1个gap, 
        # nums为等差数列时，max gap最小（等于bucket_size）
        # max gap >= bucket_size
        max_n, min_n, n = max(nums), min(nums), len(nums)
        if max_n==min_n: return 0
        bucket_size = math.ceil((max_n-min_n)/(n-1))
        if bucket_size==0: return 0
        res = 0

        # 每个桶只需要知道最大值和最小值就好
        bucket_min, bucket_max = [math.inf]*n, [-math.inf]*n
        # 装桶
        for v in nums:
            i = (v-min_n) // bucket_size  # bucket index
            bucket_min[i] = min(bucket_min[i], v)
            bucket_max[i] = max(bucket_max[i], v)
        # 桶之间比较
        prev = bucket_max[0]
        for i in range(1, n):
            if bucket_min[i]==math.inf: continue  # empty bucket
            res = max(res, bucket_min[i]-prev)
            prev = bucket_max[i]
        return res