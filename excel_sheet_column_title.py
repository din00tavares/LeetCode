class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = list()
        letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', \
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        
        nLetters = len(letters)
        division = nLetters+ 1
        while division > nLetters:
            # print(int(columnNumber/len(letters)),columnNumber%len(letters))
            remain = int(columnNumber% nLetters) -1
            if remain>= -1:
                result.insert(0, letters[remain])
            division= int(columnNumber/ nLetters)-1 if remain != -1 else int(columnNumber/ nLetters)-2
            if division< nLetters and division>= 0:
                result.insert(0, letters[division])
            else:
                columnNumber= columnNumber/ nLetters
                division= columnNumber  
        return ''.join(result)


inputs = [18279,475255,12356631,12356610,11881377,321272407,28,703,26,52,53,701,2147483647]
for input in inputs:
    r = Solution.convertToTitle(Solution,input)
    print(input, r)

