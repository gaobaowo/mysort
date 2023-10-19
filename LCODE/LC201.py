class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left < 0 or left > 2147483647:
            return
        if right < 0 or right > 2147483647:
            return
        res=left
        for i in range(left,right+1):
            res &=i
        print(res)
        return res
a=Solution()
print(a.rangeBitwiseAnd(5,2147483647))