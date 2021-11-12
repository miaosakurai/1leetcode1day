# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        new_h = ListNode(0, head)
        i = 1
        p, p_pre = head, new_h
        # find left
        while i<left:
            p_pre = p
            p = p.next
            i += 1
        pre, new_r = p_pre, p
        p_next = p.next
        # reverse left to right
        while i<right:
            p_pre = p
            p = p_next
            p_next = p_next.next
            # reverse
            p.next = p_pre
            i += 1        
        # pre -> new_l(p)
        # new_r -> post
        pre.next = p
        new_r.next = p_next
        return new_h.next
        
        