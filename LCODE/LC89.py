class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        result = []
        for index in range(2 ** n):
            result.append(index ^ index >> 1)
        return result