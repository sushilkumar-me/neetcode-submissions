class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0 
        
        cnt = 1 
        
        s = set(nums)
        for i in range(len(nums)): 
            c = 1 
            while nums[i]+1 in s: 
                c += 1
                nums[i] += 1
            cnt = max(cnt, c)
        
        return cnt

        
        