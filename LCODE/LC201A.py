class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left < 0 or left > 2147483647:
            return
        if right < 0 or right > 2147483647:
            return
        tmp = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            tmp += 1
        result = left << tmp
        return result
a=Solution()
print(a.rangeBitwiseAnd(5,7))