from abc import abstractproperty


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        np = list()
        np = [x for x in p]
        plist= list()
        nl = list()
        append_next = False
        for p in np:
            if p != '*' or append_next:
                plist.append(p)
                append_next = False
            else:
                append_next = True
                if len(plist) > 1:
                    nl.append(plist[:-1])
                    plist = [plist[-1]]


            
            
           
            
        
            


        match, i = True, 0
        for l in range(len(p)):
            try:
                if i >= len(p):
                    break
                check = s[l]
                if p[i] == '.' or check == p[i] or (p[i] == '*' and (p[i-1] == '.' or p[i-1] == check)):
                    i += 1
                    continue
                else:
                    try:
                        if p[i + 1] == "*" and check == p[i + 2]:
                            p = p[2:]
                            i += 1
                            continue
                        else:
                            match = False
                            break
                    except:
                        match = False
                        break
            except IndexError:
                match = False
                if p[-2] == '*' and p[-1] == check:
                    match = True
        if len(s) > i and match:
            if p[-1] == '*':
                if p[-2] != '.':
                    for r in range(i, len(s)):
                        if p[-2] != s[i]:
                            match = False
                            break
                        i += 1
            else:
                match = False
        return match


inputs = [["aaca","ab*a*c*a"],['ac', '.*c'], ['ab', '.*c'],['aaa','aaaa'],['abcdef', 'abc.*'], ['abccccccccc', 'abc*'], ["aaaa", "a*"], ["aa", "a"], ["aa", "a*"],
          ["ab", ".*"], ["aab", "c*a*b"], ["mississippi", "mis*is*p*."]]
for s, p in inputs:
    r = Solution.isMatch(Solution, s, p)
    print(s, p, r)
