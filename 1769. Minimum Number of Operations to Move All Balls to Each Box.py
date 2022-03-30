class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l_count, l_ans = 0, 0
        res = [0] * len(boxes)
        for i in range(len(boxes)):
            l_ans += l_count
            res[i] += l_ans
            l_count += int(boxes[i])
        
        r_count, r_ans = 0, 0
        for i in reversed(range(len(boxes))):
            r_ans += r_count
            res[i] += r_ans
            r_count += int(boxes[i])
        
        return res
            