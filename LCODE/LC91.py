class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s[0] == '0':
            return 0
        length = len(s)
        counter = 1
        auxiliary_counter = 1
        if int(s) <= 10:
            return 1
        elif 10 < int(s) <= 26:
            if int(s) == 20:
                return 1
            else:
                return 2
        else:
            for index in range(1, length):
                if s[index] == '0':
                    if s[index - 1] == '1' or s[index - 1] == '2':
                        counter = auxiliary_counter
                    else:
                        return 0
                else:
                    if s[index - 1] == '1'  or (s[index - 1] == '2' and '1' <= s[index] <= '6'):
                        auxiliary = counter
                        counter += auxiliary_counter
                        auxiliary_counter = auxiliary
                    else:
                        auxiliary_counter = counter
        return counter