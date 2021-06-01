class Solution:
    def reverse(self, x: int) -> int:
        if type(x) != int:
            raise Exception(ValueError, "Value must be int.")

        r = int(str(abs(x))[::-1])
        if r> 2**31-1:
            r = 0
        if x< 0:
            r *= -1
        return r



numbers = {123,-123,120,0,2546,213518,-513548,2147483647}
for x in numbers:
    y = Solution.reverse(Solution,x)
    print(x,y)