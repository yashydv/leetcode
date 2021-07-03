class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:

        if target in nums:

            return nums.index(target)

        mid = len(nums) // 2

        lo = 0

        hi = len(nums) - 1

        if (target > nums[len(nums)-1]):

            return len(nums)

        elif (target < nums[0]):

            return 0

        while (hi - lo) != 1:

            if (target < nums[mid]):

                hi = mid

            else:

                lo = mid

            mid = (hi - lo) // 2 + lo

        return lo +1
