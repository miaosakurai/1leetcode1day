from collections import Counter, defaultdict

class Solution:
    # The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
    # the beauty of "abaacc" is 3 - 1 = 2
    # Given a string s, return the sum of beauty of all of its substrings.
    # len(s)<3: return 0
        
    # bf Counter, O(n^2)
    def beautySum1(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                c = Counter(s[i:j+1])  # Counter size<=26, 可以算常数时间
                res += c.most_common()[0][1]-c.most_common()[-1][1]
        return res
        
    def beautySum_ref(self, s: str) -> int:
        ans = 0 
        for i in range(len(s)):
            freq = [0]*26
            for j in range(i, len(s)):
                freq[ord(s[j])-97] += 1
                ans += max(freq) - min(x for x in freq if x)
        return ans 

    # 试图优化每次创建Counter和most_common排序的步骤 
    # base_c: base counter that start from s[0]
    # other counter is branch_c
    # a b a a c c
    # ^ ^ ^        base_c
    # ^ ^ ^ ^      base_c
    #   ^ ^ ^
    # ^ ^ ^ ^ ^    base_c
    #   ^ ^ ^ ^
    #     ^ ^ ^
    # ^ ^ ^ ^ ^ ^  base_c
    #   ^ ^ ^ ^ ^
    #     ^ ^ ^ ^
    #       ^ ^ ^

    def beautySum2(self, s: str) -> int:
        if len(s)<3: return 0
        res = 0
        base_c = Counter(s[:3])
        cur_l = base_c.most_common()
        cur_max, cur_min = cur_l[0][1], cur_l[-1][1]
        res += cur_max-cur_min

        for end in range(3, len(s)):
            base_c[s[end]]+=1
            cur_l = base_c.most_common()
            cur_max, cur_min = cur_l[0][1], cur_l[-1][1]
            res += cur_max-cur_min
            
            branch_c = base_c.copy()
            for start in range(1, end-1):    
                branch_c -= Counter(s[start-1])
                cur_l = branch_c.most_common()
                cur_max, cur_min = cur_l[0][1], cur_l[-1][1]
                res += cur_max-cur_min
                
        return res

    def beautySum4(self, s: str) -> int:
        if len(s)<3: return 0
        res = 0
        base_c = defaultdict(int)
        for i in range(3):
            base_c[s[i]]+=1
        base_l = sorted(base_c.keys(), key=lambda x: base_c[x]) # 升序
        res += base_c[base_l[-1]]-base_c[base_l[0]]

        for end in range(3, len(s)):
            if s[end] not in base_c:
                base_c[s[end]]+=1
                base_l.insert(0, s[end])
            else:
                base_c[s[end]]+=1
                i = base_l.index(s[end])
                # update base_l order
                for j in range(base_l.index(s[end])+1, len(base_l)):
                    if base_c[base_l[i]]>base_c[base_l[j]]:
                        base_l[i], base_l[j] = base_l[j], base_l[i]
                        i+=1

            res += base_c[base_l[-1]] - base_c[base_l[0]]
            branch_c = base_c.copy()
            branch_l = base_l.copy()
            for start in range(1, end-1):    
                branch_c[s[start-1]] -= 1
                if branch_c[s[start-1]]<=0:
                    del branch_c[s[start-1]]
                    branch_l.remove(s[start-1])
                else:
                    i = branch_l.index(s[start-1])
                    for j in reversed(range(branch_l.index(s[start-1]))):
                        if branch_c[branch_l[i]]<branch_c[branch_l[j]]:
                            branch_l[i], branch_l[j] = branch_l[j], branch_l[i]
                            i-=1
                res += branch_c[branch_l[-1]] - branch_c[branch_l[0]]
        return res

