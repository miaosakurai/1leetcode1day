class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wd = set(wordDict)
        res = []
        for i in range(1, len(s)):
            if s[:i] in wd:
                tmp_res = self.wordBreak(s[i:], wordDict)
                for v in tmp_res:
                    res.append(s[:i]+" "+v)
        if s in wd:
            res.append(s)
        return res
        