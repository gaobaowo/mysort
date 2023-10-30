class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p,q = 0,0
        sorted = []
        while p < m or q < n:
            if p == m :
                sorted.append(nums2[q])
                q += 1
            elif q == n :
                sorted.append(nums1[p])
                p += 1
            elif nums1[p] < nums2[q]:
                sorted.append(nums1[p])
                p += 1
            else:
                sorted.append(nums2[q])
                q += 1
        nums1[:] = sorted