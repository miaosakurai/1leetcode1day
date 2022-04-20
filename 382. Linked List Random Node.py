# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random 

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.l = []
        self.count = 0
        p = head
        while p:
            self.l.append(p.val)
            self.count+=1
            p = p.next

    def getRandom(self) -> int:
        return self.l[random.randint(0, self.count-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()