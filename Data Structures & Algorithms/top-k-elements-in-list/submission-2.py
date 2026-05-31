class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} 
        for i in range(len(nums)): 
            if nums[i] not in d: 
                d[nums[i]] = 1 
            else: 
                d[nums[i]] += 1
        
        l = list(d.keys()) 
        def freq(x): 
            return d[x]
        l = sorted(l, key=freq, reverse=True)
        return l[0:k]
