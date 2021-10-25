class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3: return False
        n = len(arr)
        left = 0
        right = n-1
        for i in range(1, n):
            if arr[i]<=arr[i-1]:
                left = i-1
                break
        for i in reversed(range(n-1)):
            if arr[i]<=arr[i+1]:
                right = i+1
                break
                
        return left==right


    def validMountainArray2(self, arr: List[int]) -> bool:
        if len(arr)<3: return False
        n, m = len(arr), 0
        for i in range(1, n):
            if arr[i] <= arr[i-1]:
                m = i-1
                break
        return m!=0 and all(arr[i+1]<arr[i] for i in range(m, len(arr)-1)) 