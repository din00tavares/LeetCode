class Solution:
    def romanToInt(self, s: str) -> int:
        roman =  {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}



tests = ('III','IV', 'IX','MCM','LVIII','MCMXCIV','MMMCMXCIX','MMMCCLXXXVII')
for test in tests:
    r = Solution.romanToInt(Solution,test)
    print(test, r)
