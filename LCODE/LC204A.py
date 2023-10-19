import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        prim={2}
        for i in range(2,n):
            for j in prim:
                if (i%j==0):
                    break
            else:
                prim.add(i)
        print(list(prim))
        return len(prim)
a=Solution()
print(a.countPrimes(99979))