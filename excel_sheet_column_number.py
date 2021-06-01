class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        r = list()
        for n, l in enumerate(columnTitle):
            # print(l, letters.index(l.upper()) + 1)
            r.append(letters.index(l.upper()) + 1)
            # if len(columnTitle) == 1:
            #     r = letters.index(l) + 1
            # elif n + 1 == len(columnTitle):
            #     r += letters.index(l) + 1
            # else:
            #     r = (letters.index(l)) * len(letters) + letters.index(l) + 1

        return r


# inputs= ['ALL', 'Z', 'AA', 'ZY', 'AZ', 'AAA', 'FXSHRXW', 'DANI', 'DINO']
inputs= ['ALL', 'AB', 'AAA', 'Z', 'AZ', 'BA', 'ZY', 'FXSHRXW']
inputs= ['A', 'AA', 'AAA', 'AAAA', 'AAAAA', 'F', 'FF', 'FFF','FFFF','FFFFF']

for input in inputs:
    r = Solution.titleToNumber(Solution, input)
    print(input, r, sep= '|')
