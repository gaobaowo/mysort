class Solution:
    def countPrimes(self, n: int) -> int:
        counter=0
        for i in range(2,n):
            for j in range(2,i):
                if (i%j==0):
                    break
            else:
                counter+=1
        return counter
a=Solution()
print(a.countPrimes(10))