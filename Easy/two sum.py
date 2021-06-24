class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		idx_1, idx_2 = 0,1
		first={}
		for i,  item in enumerate(nums):
			if (target-item) in first:
				return [first[target-item], i]
				break
			first[item] = i
