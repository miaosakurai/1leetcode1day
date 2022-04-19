import re
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 多个字符split string: 用正则表达式
        cs = list(map(int, re.split('\+|-|\*', expression)))
        ops = []
        for i in range(len(expression)):
            if expression[i] in {"+", "-", "*"}:
                ops.append(expression[i])
        n = len(cs)
        dp = [[[] for i in range(n)] for j in range(n)]
        
        def op_func(a, b, c):
            if c == '+':
                return a+b
            elif c == '-':
                return a-b
            elif c == '*':
                return a*b
            
        def helper(l, r):
            if len(dp[l][r])>0:
                return dp[l][r]
            if l==r: 
                dp[l][r].append(cs[l])
            if r-l==1:
                dp[l][r].append(op_func(cs[l], cs[r], ops[l]))
            else:
                for i in range(l, r):
                    l_res = helper(l, i)
                    r_res = helper(i+1, r)
                    for v1 in l_res:
                        for v2 in r_res:
                            dp[l][r].append(op_func(v1, v2, ops[i]))
            return dp[l][r]
        return helper(0, n-1)