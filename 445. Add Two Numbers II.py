import ListNode
# 445. Add Two Numbers II
# Input: two non-empty linked lists representing two non-negative integers
# Output: Add the two numbers and return the sum as a linked list

# linked list, stack
class Solution:
    # approach 1: reverse then add from the ones place
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        p1 = self.reverse(l1)
        p2 = self.reverse(l2)
        
        head = None
        p = None
        carry = 0
        while p1 and p2:
            head = ListNode((p1.val+p2.val+carry)%10, p)
            p = head
            carry = 1 if (p1.val+p2.val+carry)>9 else 0
            p1 = p1.next
            p2 = p2.next
        p1 = p2 if p1 is None else p1
        
        if p1 is None:  # len(l1)==len(l2)
            if carry==0:
                return head
            else:
                return ListNode(1, head)
        
        while p1:
            head = ListNode((p1.val+carry)%10, p)
            p = head
            carry = 1 if (p1.val+carry)>9 else 0
            p1 = p1.next
            
        if carry==0:
            return head
        else:
            return ListNode(1, head)
    
    
    def reverse(self, l):
        p = l
        p_pre = None
        while p:
            p_next = p.next
            p.next = p_pre
            p_pre = p
            p = p_next
        return p_pre

    # approach 2: stack处理逆序的东西
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        self.pushAll(l1, s1)
        self.pushAll(l2, s2)
        p = None
        carry = 0
        while len(s1)>0 and len(s2)>0:
            cur_sum = s1.pop() + s2.pop() + carry
            p = ListNode(cur_sum%10, p)
            carry = 1 if cur_sum>9 else 0
        s = s1 if len(s2)==0 else s2
        if len(s)==0:  # len(s1)==len(s2)
            if carry==0:
                return p
            else:
                return ListNode(1, p)
        while len(s)>0:
            cur_sum = s.pop()+carry
            p = ListNode(cur_sum%10, p)
            carry = 1 if cur_sum>9 else 0
        if carry==0:
            return p
        else:
            return ListNode(1, p)
        
    def pushAll(self, l, s):
        while l:
            s.append(l.val)
            l=l.next