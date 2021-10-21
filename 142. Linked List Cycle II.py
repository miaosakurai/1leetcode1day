# return the node where the cycle begins
class Solution:
    # 1. hash table
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        p = head
        while p not in visited and p is not None:
            visited.add(p)
            p = p.next
        return p

    # 2. Floyd Cycle Detection Algorithm，快慢指针法
    # 如果有环，两个指针一定会在环上相遇
    # 环的长度：相遇之后，一个指针在相遇点等待，另一个指针绕一圈计算长度
    # 环的起点：
    # 【前提】
    # 到达相遇点时，slow走了n步，则fast走了2n步；假设head到环起点为k，环长度为c，相遇点与环起点距离c'
    # n = k + ac + c'
    # 2n = k + bc + c'
    # 因此 n = (b-a)c，n是环长度的倍数
    # 【算法】两个指针相遇后，把其中一个放在head，用同样速度移动，再次相遇的地方就是起点
    # 【解释】从head出发走k步后到达起点，另一个指针总共走了n+k步，因为n是环长的倍数，所以另一个指针也到达起点
    def detectCycle2(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while True:
            try:
                slow = slow.next
                fast = fast.next.next
            except:
                return None
            if slow == fast:
                break
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow