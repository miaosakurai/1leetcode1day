# super-palindrome: it is a palindrome, and it is also the square of a palindrome.
class Solution:
    # TLE
    def superpalindromesInRange_bf(self, left: str, right: str) -> int:
        # for i in sqrt(left)~sqrt(right)
        # if isPalindrome(i)
        # square = i**2
        # if isPalindrome(square): res+=1
        res = 0
        l = math.ceil(math.sqrt(int(left)))
        r = math.ceil(math.sqrt(int(right)))
        for i in range(l, r):
            if self.isPalindrome(i):
                if self.isPalindrome(i**2):
                    res+=1
        return res
            
    def isPalindrome(self, num):
        s = str(num)
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True
    
    def superpalindromesInRange(self, left: str, right: str) -> int:
        # 1 <= left.length, right.length <= 18
        # 平方根9位数之内
        # 一个一个判断太慢了，直接构建
        palindrome_list = [i for i in range(1, 10)]  # 先把1到9加进去
        for i in range(1, 10000): # 1~9999
            l_str = str(i)
            r_str = l_str[::-1]
            palindrome_list.append(l_str+r_str)  # 偶数长度回文
            for j in range(10):
                palindrome_list.append(l_str+str(j)+r_str)  # 奇数长度回文
            
        res = 0
        l = math.ceil(math.sqrt(int(left)))
        r = math.floor(math.sqrt(int(right)))
        
        for p in palindrome_list:
            if int(p)<l or int(p)>r:
                continue
            elif self.isPalindrome(int(p)**2):
                res+=1
        return res
            
    def isPalindrome(self, num):
        s = str(num)
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True