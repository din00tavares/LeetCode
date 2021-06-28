class Solution:
    def baseNeg2(self, n: int) -> str:
        result = ''
        while n != 0:
            if n % 2:
                result += '1'
                n -= 1
            else:
                result += '0'
            n //= -2
        return result[::-1] if result else '0'


numbers = (1,45,49,100,200,10,7,8135684,4684138435)
for number in numbers:
    r = Solution.baseNeg2(Solution,number)
    print(number, r)
