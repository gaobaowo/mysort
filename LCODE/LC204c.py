
class Solution:
    def countPrimes(self, n: int) -> int:
        a=[True]*n      
        res=0
        a[0]=False
        a[1]=False

        for i in range(2,n,1):
            if a[i]:
                res +=1
                j=i+i
                while j<n:
                    a[j]=False
                    j +=i
        return res
    
s=Solution()
print(s.countPrimes(499994))