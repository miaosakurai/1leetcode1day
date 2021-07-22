# 838. Push Dominoes
# 
# 从最左开始，遍历每个操作
# 左:
    # 上一个左/none：前面->左
    # 上一个右：do nothing
# 右：
    # 下一个左：后面一半右一半左
    # 下一个右/none：后面->右
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        actions_idx = []
        for i,d in enumerate(dominoes):
            if d=='L' or d=='R':
                actions_idx.append(i)
        results = list(dominoes)
        for i,a in enumerate(actions_idx):
            if dominoes[a]=='L':
                if i==0:
                    for j in range(a):
                        results[j]='L'
                elif dominoes[actions_idx[i-1]]=='L':
                    for j in range(actions_idx[i-1], a):
                        results[j]='L'
            if dominoes[a]=='R':
                if i==len(actions_idx)-1:
                    for j in range(a,len(results)):
                        results[j]='R'
                elif dominoes[actions_idx[i+1]]=='R':
                    for j in range(a+1, actions_idx[i+1]):
                        results[j]='R'
                elif dominoes[actions_idx[i+1]]=='L':
                    for j in range(a+1, a+1+(actions_idx[i+1]-a-1)//2):
                        results[j]='R'
                    for j in range(actions_idx[i+1]-(actions_idx[i+1]-a-1)//2, actions_idx[i+1]):
                        results[j]='L'
        return "".join(results)

    def pushDominoes2(self, dominoes: str) -> str:
        actions_idx = []
        for i,d in enumerate(dominoes):
            if d=='L' or d=='R':
                actions_idx.append(i)
        results = ""
        for i,a in enumerate(actions_idx):
            if dominoes[a]=='L':
                if i==0:
                    results+='L'*a
                elif dominoes[actions_idx[i-1]]=='L':
                    results+='L'*(a-actions_idx[i-1])
                results+='L'
                if i==len(actions_idx)-1: # last action
                    results+='.'*(len(dominoes)-a)
                elif actions_idx[i+1]=='R':
                    results+='.'*(actions_idx[i+1]-a)
            if dominoes[a]=='R':
                results+='R'
                if i==len(actions_idx)-1:
                        results+='R'*(len(dominoes)-a)
                elif dominoes[actions_idx[i+1]]=='R':
                        results+='R'*(actions_idx[i+1]-(a+1))
                elif dominoes[actions_idx[i+1]]=='L':
                    results+='R'*((actions_idx[i+1]-a-1)//2)
                    if (actions_idx[i+1]-a-1)%2!=0:
                        results+='.'
                    results+='L'*((actions_idx[i+1]-a-1)//2)
        return results

Solution().pushDominoes2("RR.L")