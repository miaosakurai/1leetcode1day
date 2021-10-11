class Solution:
    def twoSum_tle(self, numbers: List[int], target: int) -> List[int]:
        # O(n^2) - tle
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1, j+1]
                elif numbers[i]+numbers[j]>target:
                    break

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n) - counter
        c = Counter(numbers)
        for item in c.items(): 
            if target-item[0] in c: 
                if target-item[0]!=item[0]:
                    return [numbers.index(item[0])+1, numbers.index(target-item[0])+1]
                if target == item[0]*2 and item[1]>=2:
                    return [numbers.index(item[0])+1, numbers.index(item[0])+2]
    
    def twoSum_better(self, numbers: List[int], target: int) -> List[int]:
        # O(n) - dict
        d = {}
        for i in range(len(numbers)):
            if target-numbers[i] in d:
                return [d[target-numbers[i]]+1, i+1]
            d[numbers[i]]=i