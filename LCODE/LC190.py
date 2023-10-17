class Solution:
    def reverseBits(self, n: int) -> int:
        result=0
        for i in range(32):
            if n % 2 ==1:
                result *=2
                result += 1
            else:
                result *= 2
            print(result)
            n //=2
        return result
a=Solution()
print(a.reverseBits(3))
