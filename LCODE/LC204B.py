import math
class Solution:
    def countPrimes(self, n: int) -> int:
        prims=list(range(2,n))
        x=0
        y=0
        for  x in prims:
            if x> int(math.sqrt(n)):
                continue
            for y in prims:
                if y % x == 0:
                    if x != y:
                        prims.remove(y)
        return(len(prims))
a=Solution()
print(a.countPrimes(80049))