class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        for x in nums:
            while nums.count(x) > 1:
                nums.remove(x)
                
        return len(nums)
