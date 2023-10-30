class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n,m =len(s1),len(s2)
        if m !=n or sorted(s1) != sorted(s2):
            return False
        if n<4 and s1 ==s2:
            return True
        f = self.isScramble
        for i in range(1,n):
            if f(s1[:i],s2[:i]) and f(s1[i:],s2[i:]) or f(s1[i:],s2[:-i])and f(s1[:i],s2[-i:]):
                return True
        return False