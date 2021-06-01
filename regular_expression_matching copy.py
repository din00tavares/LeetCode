class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = self.normalize_pattern(Solution, p)
        p_idx, s_idx, match = 0, 0, True
        while s_idx < len(s):
            try:
                if '*' in pattern[p_idx]:
                    if s[s_idx] in pattern[p_idx] or '.' in pattern[p_idx]:
                        if len(s)-1 == s_idx and len(pattern)-1 >= p_idx and (s[s_idx] in pattern[-1] or '.' in pattern[-1]):
                            p_idx += 1
                        else:
                            pattern[p_idx] = pattern[p_idx][pattern[p_idx].index(s[s_idx]):] if s[s_idx] in pattern[p_idx] else pattern[p_idx][pattern[p_idx].index('.'):]
                        s_idx += 1
                    elif s[s_idx] in pattern[p_idx + 1] or '.' in pattern[p_idx + 1]:
                        p_idx += 2
                        s_idx += 1
                    else:
                        match = False
                        break
                elif s[s_idx] in pattern[p_idx] or '.' in pattern[p_idx]:
                    p_idx += 1
                    s_idx += 1
                else:
                    match = False
                    break
            except IndexError:
                match = False
                break
        if match and p_idx < len(pattern):
            for n in range(p_idx,len(pattern)):
                if '*' not in pattern[n]:
                    match = False
                    break
        return match

    def normalize_pattern(self, pattern: str) -> list:
        i = 0
        r = list()
        while i <= len(pattern):
            try:
                if pattern[i+1] == '*':
                    s = list()
                    try:
                        while i <= len(pattern) and pattern[i+1] == '*':
                            s.append(pattern[i])
                            i += 2
                    except IndexError:
                        pass
                    s.append('*')
                    r.append(s)
                else:
                    r.append(pattern[i])
                    i += 1
            except IndexError:
                try:
                    r.append(pattern[i])
                except IndexError:
                    pass
                break
        return r



inputs = [['ac', '.*c', True], ['ab', '.*c', False],["a",".*..a*",False],["a","ab*a",False],["a","ab*",True],["aaba", "ab*a*c*a", False], ['aaa', 'aaaa', False], ['abcdef', 'abc.*', True], ["aaca", "ab*a*c*a", True], ['vaca', '...a', True], 
        ['aaabcd', 'a*...', True], ['abcde', 'a*...', False], ['abccccccccc', 'abc*', True], ["aaaa", "a*", True], ["aa", "a", False], ["aa", "a*", True],
        ["ab", ".*", True], ["aab", "c*a*b", True], ["mississippi", "mis*is*p*.", False]]
for s, p, e in inputs:
    r = Solution.isMatch(Solution, s, p)
    print(s, p, e == r)

