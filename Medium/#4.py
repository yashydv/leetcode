class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
                
        n = sorted(nums1 + nums2)
        m = 0
        k = len(n)
        
        if k%2==0:
            m = (n[k//2]+n[k//2-1])/2
        else:
            m = n[k//2]
        return m
