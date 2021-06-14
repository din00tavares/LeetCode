class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Could you solve it without converting the integer to a string?
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        y = 0
        while x > y:
            y = y*10 + x % 10
            if x > y:
                x = int(x/10)
        return x == y


cases = [500000,121,90000000000009,10,-101,55,56,1001,3,105501,152545251,55025752055]
for case in cases:
    r = Solution.isPalindrome(Solution,case)
    print(case, r)
