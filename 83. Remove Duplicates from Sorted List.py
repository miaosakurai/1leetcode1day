# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        p = head
        next_p = head.next
        while p is not None:
            next_p = p.next
            while next_p is not None:
                if next_p.val == p.val:
                    next_p = next_p.next
                else:
                    break
            p.next = next_p
            p = p.next
        return head