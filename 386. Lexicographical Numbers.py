class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        if n<10:
            return list(range(1, n+1))
        l = [0 for i in range(n)]
        
        def dfs(cur_i, v):
            l[cur_i] = v
            last_i = cur_i+1
            for i in range(10):
                if l[cur_i]*10+i>n:
                    return last_i
                last_i = dfs(last_i, l[cur_i]*10+i)
            return last_i
        
        next_i = 0
        for i in range(1, 10):
            next_i = dfs(next_i, i)
        return l