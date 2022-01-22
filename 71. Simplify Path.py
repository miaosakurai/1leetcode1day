class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        tokens = path.split('/')
        # tokens = []
        # i,j = 0,0
        # while i<len(path):
        #     if path[i]!='/':
        #         j = i+1
        #         while j<len(path) and path[j]!='/':
        #             j+=1
        #         tokens.append(path[i:j])
        #         i=j+1
        #     else:
        #         i+=1
        
        for t in tokens:
            if t in {'.',''}:
                continue
            elif t=='..':
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(t)
        return '/'+"/".join(stack)