import math
## 找到每个节点gcd为1的最近的祖先节点
class Solution:
    # bf：每个节点和每个祖先算gcd O(nlogn)
    # WA: node 0是root节点，但是edges不是按顺序给的，edge两端不知道哪个是父哪个是子
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        ancestor = [-1 for i in range(len(nums))]
        ans = [-1 for i in range(len(nums))]
        for e in edges:
            ancestor[e[1]]=e[0]
        
        for i,v in enumerate(nums):
            anc_i = ancestor[i]
            while (anc_i != -1):
                if math.gcd(v, nums[anc_i])==1:
                    ans[i]=anc_i
                    break
                anc_i = ancestor[anc_i]
        return ans


    # bf：每个节点和每个祖先算gcd O(nlogn)
    # 先用adj_list存储无向边，再从root节点遍历确认边方向
    # TLE
    def getCoprimes2(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        ancestor = [-1 for i in range(len(nums))]
        ans = [-1 for i in range(len(nums))]
        
        adj_list = [[] for i in range(len(nums))]
        for e in edges:
            adj_list[e[1]].append(e[0])
            adj_list[e[0]].append(e[1])
            
        def set_anc(cur_anc):
            for v in adj_list[cur_anc]:
                if v!=ancestor[cur_anc]:
                    ancestor[v]=cur_anc
                    set_anc(v)
        set_anc(0)
        
        for i,v in enumerate(nums):
            anc_i = ancestor[i]
            while (anc_i != -1):
                if math.gcd(v, nums[anc_i])==1:
                    ans[i]=anc_i
                    break
                anc_i = ancestor[anc_i]
        return ans
            

    # 1 <= nums[i] <= 50，dfs的时候维持一个len<=50的祖先列表，新进来一个节点时，更新该节点值对应的祖先列表中信息，保证祖先列表中存的是离下一个节点最近的节点。复杂度 O(mn) m=50
    def getCoprimes_dfs(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        ancestor = [-1 for i in range(len(nums))]
        ans = [-1 for i in range(len(nums))]
        
        adj_list = [[] for i in range(len(nums))]
        for e in edges:
            adj_list[e[1]].append(e[0])
            adj_list[e[0]].append(e[1])
            
        def dfs(cur, ancs, height):
            closest = [-1,0]
            for a in ancs:
                if math.gcd(a, nums[cur])==1:
                    if closest[1]<=ancs[a][1]:
                        closest = ancs[a]
            ans[cur] = closest[0]
            # 当前节点信息加入或更新祖先列表
            ancs[nums[cur]]=[cur, height]  # ancs[value] = index, height
            for v in adj_list[cur]:
                if v!=ancestor[cur]:
                    ancestor[v]=cur
                    # 直接传ancs的话相当于兄弟共用ancs，dfs的顺序使前面的兄弟及孩子会影响当前结果，
                    # bfs的话会使祖先节点后面的节点影响当前结果
                    dfs(v, ancs.copy(), height+1)
        dfs(0, {}, 0)

        return ans