from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            i = -1
            while digits[i] == 9:
                digits[i] = 0
                i-= 1
                if abs(i)> len(digits):
                    digits.insert(0,0)
            digits[i]+= 1
        else:
            digits[-1] = digits[-1]+ 1
        return digits


x = Solution.plusOne(Solution,[1,2,3])
print(x)
x = Solution.plusOne(Solution,[4,3,2,9])
print(x)
x = Solution.plusOne(Solution,[9,9,9])
print(x)
x = Solution.plusOne(Solution,[4,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,5])
print(x)
