class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # how many types of candy in list
        return min(len(set(candyType)), len(candyType)//2)
