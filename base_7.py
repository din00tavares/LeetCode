class Solution:
    def convertToBase7(self, num: int) -> str:
        x = abs(num)
        r = str()
        while x // 7 != 0:
            r += str(x % 7)
            x = x // 7
        r += str(x % 7)
        r = r[::-1]
        return '-{}'.format(r) if num < 0 else r


numbers = (1,45,49,100,200,-10,-7,8135684,-4684138435)
for number in numbers:
    r = Solution.convertToBase7(Solution,number)
    print(number, r)
