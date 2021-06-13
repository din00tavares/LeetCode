class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = ' {}'.format(s)
        p = ' {}'.format(p)
        len_s, len_p = len(s), len(p)  
        result = [[0]*(len_p) for i_s in range(len_s)]
        result[0][0] = 1

        for i_p in range(1, len_p):
            if p[i_p] == '*' and result[0][i_p] != result[0][i_p-2]:
                result[0][i_p] = result[0][i_p-2]

        for i_s in range(1, len_s):
            for i_p in range(1, len_p):
                if p[i_p] in {s[i_s], '.'} and result[i_s][i_p] != result[i_s-1][i_p-1]:
                    result[i_s][i_p] = result[i_s-1][i_p-1]
                elif p[i_p] == "*":
                    result[i_s][i_p] = result[i_s][i_p-2] or int(result[i_s-1][i_p] and p[i_p-1] in {s[i_s], '.'})

        return bool(result[-1][-1])



inputs = [['ac', '.*c', True], ['ab', '.*c', False],["a",".*..a*",False],["a","ab*a",False],["a","ab*",True],["aaba", "ab*a*c*a", False], ['aaa', 'aaaa', False], ['abcdef', 'abc.*', True], ["aaca", "ab*a*c*a", True], ['vaca', '...a', True], 
        ['aaabcd', 'a*...', True], ['abcde', 'a*...', False], ['abccccccccc', 'abc*', True], ["aaaa", "a*", True], ["aa", "a", False], ["aa", "a*", True],
        ["ab", ".*", True], ["aab", "c*a*b", True], ["mississippi", "mis*is*p*.", False]]
for s, p, e in inputs:
    r = Solution.isMatch(Solution, s, p)
    print(s, p, e == r)
