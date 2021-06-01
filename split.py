def normalize_pattern(pattern):
    i = 0
    r = list()
    while i <= len(pattern):
        try:
            if pattern[i+1] == '*':
                s = set()
                try:
                    while i <= len(pattern) and pattern[i+1] == '*':
                        s.add(pattern[i])
                        i += 2
                except IndexError:
                    pass
                s.add('*')
                r.append(s)
            else:
                r.append(pattern[i])
                i+=1
        except IndexError:
            try:
                r.append(pattern[i])
            except IndexError:
                pass
            break
    return tuple(r)




inputs = [['vaca','...a'],['aaabcd','a*...'],['abcde','a*...'],['abcdef', 'abc.*'],["aaca","ab*a*c*a"],['ac', '.*c'], ['ab', '.*c'],['aaa','aaaa'],['abccccccccc', 'abc*'], ["aaaa", "a*"], ["aa", "a"], ["aa", "a*"],
          ["ab", ".*"], ["aab", "c*a*b"], ["mississippi", "mis*is*p*."]]
for s, p in inputs:
    r = normalize_pattern(p)
    print(p, r, len(r), len(s))
