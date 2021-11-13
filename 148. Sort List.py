# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        p = head
        while p:
            l.append([p.val, p])
            p = p.next
        l.sort(key=lambda x:x[0])
        h = ListNode()
        p = h
        for i in range(len(l)):
            p.next = l[i][1]
            p = p.next
        p.next = None
        return h.next

    # top-down merge sort: Time: O(nlogn), space: O(logn)
    def sortList_topdown(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.divide(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
        
    def divide(self, head):
        head_pre = ListNode(next=head)
        mid_pre, p = head_pre, head
        while p and p.next:
            mid_pre = mid_pre.next
            p = p.next.next
        mid = mid_pre.next
        mid_pre.next = None
        return mid

    def merge(self, left, right):
        lp, rp = left, right
        head = ListNode()
        p = head
        while lp and rp:
            if lp.val <= rp.val:
                p.next = lp
                lp = lp.next
            else:
                p.next = rp
                rp = rp.next
            p = p.next
        if lp:
            p.next = lp
        elif rp:
            p.next = rp
        return head.next