class Solution:
    # TLE
    def maxAbsValExpr_tle(self, arr1, arr2) -> int:
        res = 0
        n = len(arr1)
        for i in range(n):
            for j in range(i+1, n):
                res = max(res, abs(arr1[i]-arr1[j]) + abs(arr2[i]-arr2[j]) + (j-i))
        return res
    
    def maxAbsValExpr(self, arr1, arr2) -> int:
        res = 0
        n = len(arr1)
        max_sum_i, min_sum_i, max_sub_i, min_sub_i = 0, 0, 0, 0
        for j in range(1, n):
            cur_res = max(arr1[max_sum_i]+arr2[max_sum_i]-(arr1[j]+arr2[j])+(j-max_sum_i), 
                      arr1[max_sub_i]-arr2[max_sub_i]-(arr1[j]-arr2[j])+(j-max_sub_i), 
                      arr1[j]-arr2[j]-(arr1[min_sub_i]-arr2[min_sub_i])+(j-min_sub_i), 
                      arr1[j]+arr2[j]-(arr1[min_sum_i]+arr2[min_sum_i])+(j-min_sum_i))
            res = max(res, cur_res)
            if arr1[max_sum_i]+arr2[max_sum_i]<arr1[j]+arr2[j]:
                max_sum_i=j
            if arr1[max_sub_i]-arr2[max_sub_i]<arr1[j]-arr2[j]:
                max_sub_i=j
            if arr1[j]-arr2[j]<arr1[min_sub_i]-arr2[min_sub_i]:
                min_sub_i=j
            if arr1[j]+arr2[j]<arr1[min_sum_i]+arr2[min_sum_i]:
                min_sum_i=j

        return res

