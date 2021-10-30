import heapq
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # 用freq最大的数先init一个序列l，之后的数和当前序列l从后往前交叉排列（之后的数freq一定小于l）
        # 每次取出最大数 -> priority queue -> heapq
        c = Counter(barcodes)  
        q = []
        if len(q)==1: return [q[0]]
        # init
        for i in c:
            heapq.heappush(q, (-c[i], i))
        max_f = heapq.heappop(q)
        res = [max_f[1]] * -max_f[0]
        ins = 1  # next insert
        while len(q)>0:
            cur = heapq.heappop(q)
            # 当前元素插入cur[1]次
            for i in range(-cur[0]):
                res.insert(ins, cur[1])
                ins = (ins+2) % (len(res)+1)
        return res

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # insert效率太低
        # res一开始就初始化为n维数组，以步长为2先插入奇数位，再插入偶数位
        q = Counter(barcodes).most_common()
        res = [0] * len(barcodes)
        
        i = 0  # insert index
        for x in q:
            for j in range(x[1]):
                res[i] = x[0]
                i += 2
                if i>=len(barcodes):
                    i = 1
        return res
                
        
                    
            
            