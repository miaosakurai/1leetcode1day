# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # idea: fast-slow points, O(n) time, O(n) space
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
        

    def isPalindrome_2(self, head: Optional[ListNode]) -> bool:
        # idea: fast-slow points, reverse list, O(n) time, O(1) space
        if not head or not head.next:
            return True
        fast, slow, s_pre, s_next = head, head, None, head.next
        while fast and fast.next:
            fast = fast.next.next
            s_next = slow.next
            slow.next = s_pre
            s_pre = slow
            slow = s_next

        if fast and not fast.next:  # 奇数
            l, r = s_pre, slow.next
        else: # 偶数
            l, r = s_pre, slow

        while l:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
        