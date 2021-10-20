class Solution:
    # 递归实现，快但是麻烦
    def movesToStamp(self, stamp: str, target: str):
        # find last stamp
        res = self.sub(stamp, target, 0, 0)
        if res is None: return []
        else: return res

    def sub(self, stamp, target, l_space, r_space):
        if len(target)==0:
            return []   
        
        # check if stamp is substring of target
        for i in range(len(target)-len(stamp)+1):
            if stamp==target[i:i+len(stamp)]:
                left = self.sub(stamp, target[:i], l_space, r_space+len(target)-i)
                if left is None: return None
                right = self.sub(stamp, target[i+len(stamp):], l_space+i+len(stamp), r_space)
                if right is None: return None
                return left + right + [l_space+i]

        # check if target is substring of stamp
        for i in range(len(stamp)-len(target)+1):
            if target==stamp[i:i+len(target)]:
                if i<=l_space and len(stamp)-(i+len(target))<=r_space:
                    return [l_space-i]

        #  stamp
        #  ...target.
        #       stamp
        max_common = min(len(stamp), len(target))
        for i in reversed(range(1, max_common+1)):  # i: 当前重叠长度
            # check left edge 
            if len(stamp)-i<=l_space and stamp[len(stamp)-i:]==target[:i]:
                right = self.sub(stamp, target[i:], l_space+i, r_space)
                if right is None: return None
                return right + [l_space-(len(stamp)-i)]
            # check right edge
            elif len(stamp)-i<=r_space and stamp[:i]==target[len(target)-i:]:
                left = self.sub(stamp, target[:len(target)-i], l_space, r_space+i)
                if left is None: return None
                return left + [l_space+ len(target)-i]
            
        return None

    # greedy or 类BFS实现，参考 https://leetcode.com/problems/stamping-the-sequence/discuss/189254/Python-Greedy-and-DFS
    def movesToStamp2(self, stamp: str, target: str) -> List[int]:
        t, s, N, M = list(target), list(stamp), len(target), len(stamp)
        reversed_res = []
        changed = True
        
        def sub(i):  # target index
            for j in range(M):
                if t[i+j] != '?' and t[i+j] != s[j]: return False
            if t==['?'] * N: return False
            return True
        
        while changed:
            changed = False
            for i in range(N-M+1):
                if sub(i) and i not in reversed_res:
                    changed = True
                    reversed_res.append(i)
                    t[i:i+M] = ['?'] * M
        return reversed_res[::-1] if t==['?']*N else []

print(Solution().movesToStamp2("abc","ababc"))