class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, rm = [], []
        l = list(s)
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if len(stack)==0:
                    rm.append(i)
                else:
                    stack.pop()
        rm = sorted(rm + stack, reverse=True)
        for i in rm:
            l.pop(i)
        return "".join(l)