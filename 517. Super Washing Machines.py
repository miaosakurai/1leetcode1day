class Solution:
    # 平分list中元素最小移动数
    # 每次有多个machine移动，只能移动一件衣服

    # BF, O(n^2), TLE
    def findMinMoves(self, machines: List[int]) -> int:
        if sum(machines)==0: return 0
        # not possible
        if sum(machines)%len(machines)!=0: return -1
        target = sum(machines)//len(machines)
        
        # 传出次数：自己多出来的 + 运输过程需要经过自己的
        l_moves = [0 for i in range(len(machines))] # 需要向左传出的 = 左边一共缺少的
        r_moves = [0 for i in range(len(machines))] # 需要向右传出的 = 右边一共缺少的
        move = 0
        for i in range(len(machines)):
            l_sum = sum(machines[:i])
            r_sum = sum(machines[i+1:])
            if l_sum < target*i: # 需要向左边传的
                l_moves[i] = target*i-l_sum
            if r_sum < target*(len(machines)-i-1):  # 需要向右边传的
                r_moves[i] = target*(len(machines)-i-1)-r_sum
        
        while True:
            m_next = machines.copy()
            moved = False
            for i in range(len(machines)):
                if m_next[i]>0:
                    if l_moves[i]>0:
                        l_moves[i]-=1
                        m_next[i]-=1
                        m_next[i-1]+=1
                        moved = True
                    elif r_moves[i]>0:
                        r_moves[i]-=1
                        m_next[i]-=1
                        m_next[i+1]+=1
                        moved = True
            if not moved:
                return move
            move+=1
            machines = m_next

        return move

    # 优化1： 总move数的瓶颈应该是需要传出最多的machine, 3036 ms	
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        if sum(machines)==0: return 0
        # not possible
        if sum(machines)%n!=0: return -1
        target = sum(machines)//n
        
        # 传出次数 = 自己多出来的 + 运输过程需要经过自己的 = 向左传出的 + 向右传出的
        move = 0
        for i in range(n):
            l_sum = sum(machines[:i])
            r_sum = sum(machines[i+1:])
            l_move = target*i-l_sum if l_sum < target*i else 0  # 需要向左边传的 (左边缺少的)
            r_move = target*(n-i-1)-r_sum if r_sum < target*(n-i-1) else 0  # 需要向右边传的 (左边缺少的)
            move = max(move, l_move+r_move)
        return move

    # 优化2：减少sum()次数，88 ms
    def findMinMoves2(self, machines: List[int]) -> int:
        n = len(machines)
        m_sum = sum(machines)
        if m_sum==0: return 0
        # not possible
        if m_sum%n!=0: return -1
        target = m_sum//n
        
        # 传出次数 = 自己多出来的 + 运输过程需要经过自己的 = 向左传出的 + 向右传出的
        move = 0
        pre_m = 0
        l_sum = 0
        r_sum = m_sum
        for i in range(n):
            l_sum += pre_m
            r_sum -= machines[i]
            pre_m = machines[i]
            l_move = target*i-l_sum if l_sum < target*i else 0  # 需要向左边传的 (左边缺少的)
            r_move = target*(n-i-1)-r_sum if r_sum < target*(n-i-1) else 0  # 需要向右边传的 (左边缺少的)
            move = max(move, l_move+r_move)
        return move