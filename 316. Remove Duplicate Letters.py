## Question
# Remove duplicate letters and the result is the smallest in lexicographical order
# Input: s = "cbacdcbc"
# Output: "acdb"

## stack
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if s == "": return ""
        last_at = {}  # remaining count
        in_stack = {}
        for i,l in enumerate(s):
            in_stack[l]=False
            last_at[l] = i

        stack = [s[0]]  # locally increasing stack
        in_stack[s[0]]=True

        for i in range(1, len(s)):
            if in_stack[s[i]]: 
                continue
            while len(stack) > 0 and stack[-1] > s[i] and last_at[stack[-1]] > i:
                in_stack[stack.pop()]=False
            stack.append(s[i])
            in_stack[s[i]]=True

        return "".join(stack)