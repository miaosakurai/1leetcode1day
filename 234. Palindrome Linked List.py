# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # idea: fast-slow points
        l = []
        if not head or not head.next:
            return True
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            l.append(slow.val)
            slow = slow.next
        if fast and not fast.next:  # 奇数
            slow = slow.next
        while len(l)>0:
            if l.pop()!=slow.val:
                return False
            slow = slow.next
        return True
        