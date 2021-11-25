# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # method 1: 先把nodes存到list，再用list index重排
    def reorderList1(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next
        if len(nodes)<=2: return
        
        cur, pre = nodes[0], None
        i, j = 1, len(nodes)-1
        while i<j:
            cur.next = nodes[j]
            cur.next.next = nodes[i]
            pre = cur.next
            cur = cur.next.next
            i += 1
            j -= 1
        if i==j:
            cur.next = nodes[i]
            cur = cur.next
        cur.next = None

        
    # method 2: 旋转后半部分，再merge
    def reorderList2(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. compute length
        fake = ListNode(next=head)
        fast, slow = fake, fake
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow -> 左中
        
        # 2. reverse remain nodes
        #      a -> b -> c
        # pre cur  nex 
        pre, cur = None, slow.next
        slow.next = None
        
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        
        # 3. merge
        p1, p2 = head, pre
        while p2:
            p1_next, p2_next = p1.next, p2.next
            p1.next = p2
            p2.next = p1_next
            p1, p2 = p1_next, p2_next
        
        
        