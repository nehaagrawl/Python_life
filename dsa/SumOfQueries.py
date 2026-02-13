class Solution:
    def querySum(self, n, arr, q, queries):
        prefix=[0]*n
        prefix[0]=arr[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+arr[i]
        result=[]
        for i in range(0,2*q,2):
            l=queries[i]
            r=queries[i+1]
            
            if l==1:
                result.append(prefix[r-1])
            else:
                result.append(prefix[r-1]-prefix[l-2])
        return result
    
obj=Solution()
n = 4
arr = [1, 2, 3, 4]
q = 2 
queries = [1, 4 ,2 ,3]
print(obj.querySum(n,arr,q,queries))
