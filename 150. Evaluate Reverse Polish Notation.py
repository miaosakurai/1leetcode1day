class Solution:
    # tokens in postorder
    # 循环计算
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        while len(tokens)>1:
            i = len(tokens)-1
            while i>=2:
                if tokens[i] in ops and tokens[i-1] not in ops and tokens[i-2] not in ops:
                    tokens[i-2] = self.op(int(tokens[i-2]), int(tokens[i-1]), tokens[i])
                    tokens.pop(i)
                    tokens.pop(i-1)
                    i -= 2
                    # print(tokens)
                else:
                    i-=1
                    
        return tokens[0]
    
    def op(self, a, b, op):
        if op=='+':
            return a+b
        elif op=='-':
            return a-b
        elif op=='*':
            return a*b
        else:
            if a/b<0:
                return math.ceil(a/b)
            else:
                return math.floor(a/b)
            # return int(float(a)/b) 或 int(a/b)
            # int(): 很多地方说是向下取整，但其实是向零取整，即直接舍弃浮点位的取整方法

    # stack
    def evalRPN_2(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        st = []
        
        for i in range(len(tokens)):
            if tokens[i] in ops:
                b, a = st.pop(), st.pop()
                st.append(self.op(a, b, tokens[i]))
            else:
                st.append(int(tokens[i]))
        return st[0]
    