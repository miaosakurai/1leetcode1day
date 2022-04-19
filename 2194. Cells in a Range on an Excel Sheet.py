class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, r1, c2, r2 = s[0], s[1], s[3], s[4]
        res = []
        for i in range(ord(c2)-ord(c1)+1):
            for j in range(int(r2)-int(r1)+1):
                res.append(chr(ord(c1)+i)+str(int(r1)+j))
        return res