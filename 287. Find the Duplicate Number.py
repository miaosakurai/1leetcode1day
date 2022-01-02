class Solution:
    def findDuplicate_set(self, nums: List[int]) -> int:
        # T: O(n), S: O(n)
        s = set()
        for i,v in enumerate(nums):
            if v in s:
                return v
            else:
                s.add(v)
        
    def findDuplicate_neg(self, nums: List[int]) -> int:
        # negative marking (在nums上用正负表示visited，节省O(n)的空间)
        # T: O(n), S: O(1)
        res = 0
        for v in nums:
            cur = abs(v)
            if nums[cur]<0:
                res = cur
                break
            nums[cur] =- nums[cur]

        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=-nums[i]
        return res

    def findDuplicate_hash(self, nums: List[int]) -> int:
        # Hashmap：把每个数字map到相应的index，这样相同的数字就会遇到
        # T: O(n), S: O(n) -> 递归最多可能同时产生n次函数调用
        def store(nums, cur):
            if nums[cur] == cur:
                return cur
            nxt = nums[cur]
            nums[cur] = cur
            return store(nums, nxt)
        
        return store(nums, 0)
    
    def findDuplicate_hash2(self, nums: List[int]) -> int:
        # Hashmap不使用递归
        # T: O(n), S: O(1)
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
            # 这里要注意交换顺序不能反过来：如果是先赋值nums[0]，那么nums[nums[0]]中的nums[0]会使用修改后的值
        return nums[0]
       