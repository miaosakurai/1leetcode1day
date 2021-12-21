# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # binary search
        start, end = 1, n
        while start<end:
            mid = (start+end)//2
            if isBadVersion(mid):
                end=mid
            else:
                start=mid+1
        return end
        
        # O(n):
        # bad = 1
        # for i in range(1, n+1):
        #     if isBadVersion(i):
        #         bad = i
        #         break
        # return bad