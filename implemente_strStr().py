class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


x = Solution.strStr(Solution,'aaaaaaaaa','bba')
print(x)
x = Solution.strStr(Solution,'hello','ll')
print(x)
x = Solution.strStr(Solution,'','')
print(x)
x = Solution.strStr(Solution,'haystack and needle consist of only lower-case English characters','on')
print(x)