class Solution:
    def maxArea(self, height: List[int]) -> int:
        M = 0
        i, j = 0, len(height)-1
        while i < j:
            a, b = height[i], height[j]
            M = max(min(a, b) * (j - i), M)
            if a > b:
                j -= 1
            else:
                i += 1
        return M
