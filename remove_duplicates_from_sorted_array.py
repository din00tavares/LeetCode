from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i= 0
        for n in nums:
            try:
                while nums[i+1] == n:
                    nums.remove(n)
            except:
                break
            i+= 1
            
        return len(nums), nums

        


l,n = Solution.removeDuplicates(Solution,[0,0,1,1,1,2,3,4,4,4])
print(l,n)
l,n = Solution.removeDuplicates(Solution,[1,1,2])
print(l,n)
l,n = Solution.removeDuplicates(Solution,[-501,-501,-500,-450,-450,-5,-5,-5,2,2,2,2,5,5,5,5,450,450,500,501,501])
print(l,n)