class Solution:
    def hammingWeight(self, n: int) -> int:
        counter=0
        for i in range(32):
            if n % 2 ==1:
                counter += 1
            n = n // 2
        return counter 
v=Solution()
print(v.hammingWeight(32768))
